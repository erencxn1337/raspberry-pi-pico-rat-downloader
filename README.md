# 🦅 Project Shadow-HID: Advanced Command Injection Engine

[![Python](https://img.shields.io/badge/Language-CircuitPython-blue.svg)](https://circuitpython.org)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11-blue.svg)](https://www.microsoft.com/windows)
[![Category](https://img.shields.io/badge/Category-Red_Teaming-red.svg)](#)

A high-performance **HID (Human Interface Device) Injection Engine** designed for rapid payload delivery, privilege escalation, and security infrastructure bypass during authorized Red Team operations.

---

## 🛡️ Legal & Ethical Usage Warning
> [!IMPORTANT]
> This software is provided exclusively for **authorized penetration testing** and **educational research**. Any unauthorized use against systems without prior explicit consent is strictly prohibited and may violate local and international laws. The developer assumes no liability for misuse.

---

## 🔬 Core Capabilities

### ⚡ Accelerated Privilege Escalation
Utilizes precise timing logic to trigger **Administrative UAC (User Account Control)** elevation and implements automated keystroke confirmation to secure high-integrity execution environments.

### 🧤 Native Defense Evasion (Defender Killer)
Implements real-time manipulation of the Windows Malware Protection Engine. It dynamically injects exclusion paths and process-level exceptions to ensure the payload remains unmonitored by **Windows Defender** and **AMSI**.

### 🌑 Stealth Deployment Architecture
*   **Zero-Disk Footprint:** Initial command injection occurs entirely in memory via PowerShell reflection triggers.
*   **Automated Cleanup:** Forcibly terminates telemetry-providing processes (PowerShell/CMD) immediately upon operation completion.
*   **Encrypted Sync:** Designed to integrate seamlessly with **AES-256 encrypted payloads** (e.g., Echo Crypter builds).

---

## 🛠️ Technical Implementation

### Prerequisite Configuration
1.  **Hardware:** Raspberry Pi Pico (RP2040), Digispark, or any CircuitPython-compliant HID controller.
2.  **Dependencies:** Mount the `adafruit_hid` library to the device `/lib` directory.
3.  **Keymap:** Default configuration is optimized for **US-English** (KeyboardLayoutUS).

### Deployment Steps
1.  Format your microcontroller with **CircuitPython 8.x** or higher.
2.  Deploy the optimized `code.py` to the root directory.
3.  Modify the `IWR` (Invoke-WebRequest) string within the `commands` array to mirror your secure C2 infrastructure or repository link.

---

## 📡 Operational Flowchart

1. **Initialization:** 2000ms hardware handshake delay.
2. **Phase I:** Trigger "Run" dialogue -> Launch PowerShell baseline.
3. **Phase II:** Request `runAs` verb -> Administrative elevation prompt.
4. **Phase III:** Automate UAC bypass (Signal: `Alt + Y`).
5. **Phase IV:** Registry-level exclusion injection (Defender/AMSI bypass).
6. **Phase V:** Binary ingestion -> Remote execution -> Persistent link established.
7. **Cleanup:** Process tree termination and trace purging.

---

## 🤝 Open Source Contribution
Contributions to improve execution timing or support for localized keyboard layouts are welcome. Please submit a Pull Request following our code-style guidelines.

---
*Developed for Advanced Security Research and Professional Red Teaming.*
