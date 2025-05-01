# borshevik-control-center

This is a patched version of [GNOME Control Center](https://gitlab.gnome.org/GNOME/gnome-control-center) customized for [Borshevik OS](https://github.com/komorebithrowsatable/komorebi-os).

It includes branding and configuration changes tailored to the Borshevik desktop experience.

## ✨ Key Modifications

- **Borshevik Branding**
  - Custom `os-release` ID recognition (`borshevik`)
  - Custom logo icon displayed in the system info panel (`borshevik-logo-icon.svg`)
- **User Experience Enhancements**
  - Variable Refresh Rate (VRR) enabled by default
  - Fractional scaling enabled by default (experimental)

## 🎯 Purpose

This repository exists to maintain a patched `gnome-control-center` RPM for integration with the [Borshevik OS](https://github.com/komorebithrowsatable/komorebi-os) image.

It is rebuilt via [Fedora COPR](https://copr.fedorainfracloud.org) and distributed as a drop-in replacement for the stock Fedora `gnome-control-center`.
