const { test, expect } = require('@playwright/test');

test('Check header', async ({ page }) => {
    // await page.goto('http://localhost:8080');  // you can replace this URL with any page that includes the header
    await page.goto('https://nikolay-x-exam.onrender.com');
    const homeLink = await page.$('a[href="/"]');
    const text = await homeLink.textContent();
    // expect(text).toBe('Boardgame Collection');
    expect(text).toBe('Home');
  });
  