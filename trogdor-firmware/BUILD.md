# trogdor-firmware build notes

This document explains how to refresh the payload, generate the source tarball, and build the RPM locally.

## Prerequisites

- Fedora tooling: `dnf install rpm-build rpmdevtools`.
- Working directory: this repository cloned to `/home/craig/Documents/ChromebookFirmware`.
- Firmware blobs staged under `packaging/trogdor-firmware/SOURCES/trogdor-firmware-<date>/usr/lib/firmware`.

## Update workflow

1. **Refresh the payload**k
   - Copy new firmware blobs into `packaging/trogdor-firmware/SOURCES/trogdor-firmware-<date>/usr/lib/firmware`.
   - Adjust systemd units (for example `usr/lib/systemd/system/rmtfs-trogdor.service`) in the same tree when behaviour changes.
   - Preserve symlinks (`venus.mdt`, `rt3070.bin`) so that they match ChromeOS.
   - Update `packaging/trogdor-firmware/manifest.txt` and `docs/trogdor-firmware-files.md` with file sizes, hashes, and provenance.

2. **Bump the version**
   - Choose the new date-based version (format `YYYY.MM.DD`).
   - Rename the payload directory to `trogdor-firmware-<newversion>` to match the planned tarball name.
   - Edit `packaging/trogdor-firmware/trogdor-firmware.spec`:
     - Set `Version:` to the new value.
     - Update the `%changelog` with the new release entry.

3. **Generate the source archive**
   - Run:
     ```bash
     cd /home/craig/Documents/ChromebookFirmware/packaging/trogdor-firmware/SOURCES
     tar -czf trogdor-firmware-<version>.tar.gz trogdor-firmware-<version>
     ```
   - Copy the tarball into your RPM build tree if you use the per-user `rpmbuild` layout:
     ```bash
     rpmdev-setuptree            # only needed once
     cp trogdor-firmware-<version>.tar.gz ~/rpmbuild/SOURCES/
     cp ../trogdor-firmware.spec ~/rpmbuild/SPECS/
     ```

4. **Build the RPM**
   - Execute:
     ```bash
     rpmbuild -bb ~/rpmbuild/SPECS/trogdor-firmware.spec
     ```
   - The resulting RPM can be found under `~/rpmbuild/RPMS/noarch/`.

5. **Verify contents**
   - List files inside the RPM:
     ```bash
     rpm -qlp ~/rpmbuild/RPMS/noarch/trogdor-firmware-<version>-1.fc$(rpm -E %fedora).noarch.rpm
     ```
   - Confirm SHA256 values match `manifest.txt` (e.g. using `sha256sum` over the buildroot prior to packaging).

## Distribution

- Publish the RPM in a personal repository or install with `dnf install ./trogdor-firmware-<version>-1.fc*.noarch.rpm`.
- When updating, repeat the steps above and increment the release or version as appropriate. For simple blob refreshes on the same day, bump the `Release:` field instead of `Version:`.

