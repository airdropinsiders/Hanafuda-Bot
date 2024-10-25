# Hanafuda Auto Deposit + AutoTap Script

Skrip Python ini digunakan untuk mengirimkan transaksi otomatis berupa deposit ETH ke kontrak tertentu di jaringan HANA Network. Skrip menggunakan `web3.py` untuk koneksi blockchain dan `colorama` untuk tampilan warna di terminal.

## Fitur

- Pengiriman transaksi otomatis dalam batch dari beberapa alamat
- Notifikasi kesalahan jika terjadi kegagalan transaksi
- Pengecekan dan penyesuaian nonce untuk setiap transaksi
- Pencatatan waktu eksekusi untuk setiap transaksi
- Output berwarna untuk kemudahan pemantauan

## Prasyarat

- Python 3.x
- Akses ke node Ethereum (disarankan RPC URL yang valid, seperti Infura atau node sendiri)

## Instalasi

1. **Clone repositori ini:**
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
