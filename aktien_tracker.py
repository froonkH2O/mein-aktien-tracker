import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Liste mit interessanten Aktien 2026 (KI, Energie etc.)
aktien = ["NVDA", "TSLA", "MSFT", "GEV", "BE"]

print("=== Aktien-Tracker mit 200-Tage SMA ===\n")

for aktie in aktien:
    print(f"Lade Daten für {aktie}...")
    data = yf.download(aktie, period="1y", progress=False)
    
    if not data.empty and len(data) >= 200:
        data['SMA_200'] = data['Close'].rolling(window=200).mean()
        
        aktueller_preis = data['Close'].iloc[-1]
        sma_200 = data['SMA_200'].iloc[-1]
        
        print(f"{aktie}:")
        print(f"  Aktueller Preis: {aktueller_preis:.2f} USD")
        print(f"  200-Tage-Durchschnitt: {sma_200:.2f} USD")
        
        if aktueller_preis > sma_200:
            print("  → Preis ist ÜBER dem Durchschnitt (bullisch)")
        else:
            print("  → Preis ist UNTER dem Durchschnitt")
        print("---")
        
        # Chart speichern
        plt.figure(figsize=(10,5))
        plt.plot(data.index, data['Close'], label='Aktienpreis')
        plt.plot(data.index, data['SMA_200'], label='200-Tage SMA', color='red')
        plt.title(f"{aktie} - Preis vs 200-Tage SMA")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{aktie}_chart.png")
        print(f"Chart gespeichert: {aktie}_chart.png\n")
    else:
        print(f"Nicht genug Daten für {aktie}\n")

print("Fertig! Schau dir die .png Dateien im Ordner an.")