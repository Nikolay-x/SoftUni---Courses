const { test, expect } = require('@playwright/test');

test('Check boardgames page', async ({ page }) => {
    // await page.goto('http://localhost:8080/collection');
    // await page.goto('http://localhost:8080/boardgames');
    await page.goto('https://nikolay-x-exam.onrender.com/boardgames');
    const list = await page.$('ul');
    expect(list).toBeTruthy();
  });
  