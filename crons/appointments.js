const { schedule } = require("@netlify/functions");
const chromium = require('chrome-aws-lambda');
const puppeteer = require('puppeteer-core');
const nodemailer = require("nodemailer");
const mg = require("nodemailer-mailgun-transport");

const transporter = nodemailer.createTransport(
  mg({
    auth: {
      api_key: process.env.MAILGUN_API_KEY,
      domain: process.env.MAILGUN_DOMAIN,
    },
  })
);

const handler = async function(event, context) {
  console.log(process.version)
  const browser = await puppeteer.launch({
    args: chromium.args,
    defaultViewport: chromium.defaultViewport,
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || await chromium.executablePath,
    headless: chromium.headless,
    ignoreHTTPSErrors: true,
  });
  const page = await browser.newPage()
  await page.goto(process.env.APPOINTMENTS_URL);
  await page.waitForSelector("#username-label")
  await page.type("#username", process.env.ACCOUNT_USERNAME)
  await page.type("#password", process.env.ACCOUNT_PASSWORD)
  await page.click("button[type='submit']")
  await page.waitForSelector("button[name='view_search']")
  const match = (await page.content()).match(/n'est actuellement disponible/gi)
  if (match) {
    console.log("no appointment found")
    return { statusCode: 404 }
  }
  const info = await transporter.sendMail({
    from: `mailgun@${process.env.MAILGUN_DOMAIN}`,
    to: process.env.MAILGUN_SENDER,
    subject: "City Hall appointment is ready!",
    text: process.env.APPOINTMENTS_URL,
  });
  console.log(`Alert sent: ${info.messageId}`);
  await browser.close();
  return { statusCode: 200 }
};

exports.handler = schedule("*/10 * * * *", handler);
