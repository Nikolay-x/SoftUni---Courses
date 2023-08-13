const { test, expect } = require('@playwright/test');

test('Check footer', async ({ page }) => {
    // await page.goto('http://localhost:8080');  
    await page.goto('https://nikolay-x-exam.onrender.com');  
    const footer = await page.$('footer');
    const text = await footer.textContent();
    // expect(text).toContain('© 2023 - Software Engineеring and DevOps exam preparation');
    expect(text).toContain('© 2023 - Software Engineering and DevOps regular exam');
  });
  