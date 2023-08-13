const { test, expect } = require('@playwright/test');

test('Check add boardgame page', async ({ page }) => {
    // await page.goto('http://localhost:8080/add-boardgame');
    await page.goto('https://nikolay-x-exam.onrender.com/add-boardgame');
    const form = await page.$('form');
    expect(form).toBeTruthy();
  });
  