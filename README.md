# PowerShell HID Downloader & Defender Bypass

A specialized HID injection script for Windows systems that automates administrative privilege escalation, security exclusion, and payload deployment.

---

## 🏗️ Core Workflow

This script executes the following sequence via automated keystrokes:

1.  **Handshake:** 2-second initial delay for hardware synchronization.
2.  **Access:** Triggers `Win + R`, launches a baseline `powershell` instance.
3.  **Elevation:** Requests high-integrity execution via `Start-Process powershell -Verb runAs`.
4.  **UAC Authorization:** Automates the "User Account Control" prompt confirmation using `Alt + Y`.
5.  **Security Suppression:** 
    *   Adds an exclusion path for the `%APPDATA%` directory to Windows Defender.
    *   Adds a process-specific exclusion for the target binary (`windowss.exe`).
6.  **Ingestion:** Downloads the remote payload from GitHub to the hidden AppData folder.
7.  **Execution:** Launches the downloaded binary in the background.
8.  **Cleanup:** Terminates all active PowerShell processes to purge the execution history.

---

## 🛠️ Technical Specifications

### Hardware Requirements
*   Microcontroller compatible with **CircuitPython** (e.g., Raspberry Pi Pico, Digispark).
*   **HID Library:** `adafruit_hid` installed in the `/lib` directory.

### Target Environment
*   **Operating System:** Windows 10 / 11.
*   **Keyboard Layout:** US-English.

### Implementation Checklist
1. Update the `commands` array with your specific GitHub raw URL or C2 bridge.
2. Ensure the destination filename in the script matches your deployment requirements.
3. Upload `code.py` to the root of the microcontroller.

---

## ⚖️ Legal Disclaimer
This tool is for **authorized security testing** and **educational research** only. Unauthorized access to computer systems is illegal. The user is solely responsible for compliance with local laws.
