# Hanafuda Auto Deposit + AutoTap Script

This Python script is used to send automatic transactions in the form of ETH deposits to certain contracts on the HANA Network. The script uses `web3.py` for blockchain connection and `colorama` for color display in the terminal.

## Register with HanaFuda (Hana Network)

- https://hanafuda.hana.network
- 𝗨𝘀𝗲 𝗮𝗰𝗰𝗲𝘀𝘀 𝗰𝗼𝗱𝗲: 21OM73
- Deposit $0,5- $1 in ARB or BASE network for low gas fees
- Go to dashboard
- Earn Points via Grow and Draw Hanafuda
- WIthdraw start early Q1 2025 

## Features

- Automatic sending of transactions in batches from multiple addresses
- Error notification if a transaction fails
- Checking and adjusting nonce for each transaction
- Recording execution time for each transaction
- Colored output for easy monitoring

## Prerequisites

- Python 3.x
- Access to an Ethereum node (a valid RPC URL is recommended, such as Infura or your own node)

## Instalasi

1. **Clone Repository:**
   ```bash
   git clone https://github.com/airdropinsiders/Hanafuda-Bot.git
   cd Hanafuda-Bot
   ```
2.  **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run**
    ```bash
    python3 bot.py
    ```

## AutoTap Card

1. **Open Dev Console and paste this script**
  ```
  let count = 0;
function clickElements() {
    if (count < 1000) {
        // Check first element before clicking
        let element1 = document.querySelector('body > div > div > div:nth-child(3) > div > div.relative.z-10.grid.size-full.flex-1.grid-cols-1.grid-rows-\\[20\\%_60\\%_20\\%\\].content-center.items-center.justify-center.justify-items-center.p-6 > div.relative.flex.size-full.flex-col.items-center.justify-center > div > div > canvas');
        if (element1) {
            element1.click();
            console.log('Clicked button 1');
        } else {
            console.log('Button 1 not found');
        }

        // Wait 5 seconds then click on the second element
        setTimeout(function() {
            let element2 = document.querySelector('body > div > div > div:nth-child(3) > div > div.relative.z-10.grid.size-full.flex-1.grid-cols-1.grid-rows-\\[20\\%_60\\%_20\\%\\].content-center.items-center.justify-center.justify-items-center.p-6 > div.relative.flex.w-full.items-center.justify-center.gap-1\\.5.lg\\:gap-3 > button.flex.cursor-pointer.items-center.justify-center.font-medium.tracking-\\[0\\.24px\\].disabled\\:cursor-default.shiny-button-color-red.shiny-button.h-\\[57px\\].w-\\[224px\\].rounded-\\[8px\\].text-\\[12px\\].max-w-\\[128px\\].gap-1\\.5.sm\\:gap-3.lg\\:w-\\[224px\\].lg\\:max-w-full');
            if (element2) {
                element2.click();
                console.log('Clicked button 2');
            } else {
                console.log('Button 2 not found');
            }

            count++; // Increment the counter variable after each turn
            setTimeout(clickElements, 3000); // After 3 seconds repeat the process
        }, 3000); // Wait 3 seconds after 1st click
    }
}

// Start the process
clickElements();
```
