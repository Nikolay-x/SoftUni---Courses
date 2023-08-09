const { test, expect } = require('@playwright/test');

test('Check footer', async ({ page }) => {
    // await page.goto('http://localhost:8080');  
    await page.goto('https://nikolay-x-movies.onrender.com');  
    const footer = await page.$('footer');
    const text = await footer.textContent();
    expect(text).toContain('© 2023 - Software Engineering and DevOps exam preparation');
  });
  