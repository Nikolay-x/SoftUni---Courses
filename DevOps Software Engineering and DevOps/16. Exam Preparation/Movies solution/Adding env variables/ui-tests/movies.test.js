const { test, expect } = require('@playwright/test');

require('dotenv').config();

test('Check movies page', async ({ page }) => {
    // await page.goto('http://localhost:8080/movies');
    // await page.goto('https://nikolay-x-movies.onrender.com/movies');
    await page.goto(process.env.DEPLOYED_URL + '/movies');
    const list = await page.$('ul');
    expect(list).toBeTruthy();
  });
  