const puppeteer = require('puppeteer');

async function snatcher3080(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

    const [el] = await page.$x('/html/body/app-root/product/div[1]/div[1]/div[2]/div/product-details/div/div/div[1]/div[2]/div[3]/div[2]/div[1]/a');
    const txt = await el.getProperty('textContent');
    const rawTxt = await txt.jsonValue();

    console.log({rawTxt});

    browser.close();
}

snatcher3080("https://www.nvidia.com/en-us/shop/geforce/gpu/?page=1&limit=9&locale=en-us&category=GPU&gpu=RTX%203080")

