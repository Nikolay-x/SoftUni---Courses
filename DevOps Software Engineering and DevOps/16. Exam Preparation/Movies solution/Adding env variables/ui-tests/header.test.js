const { test, expect } = require('@playwright/test');

require('dotenv').config();

test('Check header', async ({ page }) => {
    // await page.goto('http://localhost:8080');  // you can replace this URL with any page that includes the header
    // await page.goto('https://nikolay-x-movies.onrender.com');
    await page.goto(process.env.DEPLOYED_URL);
    const homeLink = await page.$('a[href="/"]');
    const text = await homeLink.textContent();
    expect(text).toBe('Home');
  });
  