const { test, expect } = require('@playwright/test');

require('dotenv').config();

test('Check about page', async ({ page }) => {
  // await page.goto('http://localhost:8080/about');
  // await page.goto('https://nikolay-x-movies.onrender.com/about');
  await page.goto(process.env.DEPLOYED_URL + '/about');
  const heading = await page.$('h1');
  const text = await heading.textContent();
  expect(text).toBe('About');
});
