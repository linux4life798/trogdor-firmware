<!-- Generated to track ChromeOS-specific firmware required by trogdor devices. -->
# Trogdor Firmware Inventory

This table tracks firmware blobs copied from the ChromeOS wormdingler image that do **not** ship with Fedora 43. Update it whenever new binaries are added to the package.
The RPM also ships the `rmtfs-trogdor.service` unit, documented in `packaging/trogdor-firmware/manifest.txt`.

| Firmware Path (under `/usr/lib/firmware`) | Size (bytes) | Type | SHA256 / Target |
| --- | ---: | --- | --- |
| `cros-pd/README.source` | 161 | file | `33d8e4faeca46e116c6ad13d32d0e9f02615ea97821b2b9e52820d04c91207ad` |
| `cros-pd/dingdong_v1.7.317-b0bb7c9.bin` | 65536 | file | `9cdcb32fe8f678abb6170be8189005e78daec85eaa39a569c23d3b4cb33f2b9d` |
| `cros-pd/dingdong_v1.7.575-96b74f1.bin` | 65536 | file | `99f56aebbc29d43318a858121aff97c11bda1e7efff7d7755ba7b533f3b9023e` |
| `cros-pd/dingdong_v1.7.684-69498dd.bin` | 65536 | file | `15f833017de4aed4c2ba187807470d63f032717d0c74f413a961ed46ae8f22de` |
| `cros-pd/hoho_v1.7.317-b0bb7c9.bin` | 65536 | file | `9e1a1cd64fb032a639542835ebabe61061a0a7401714daf42106b6912b6cc467` |
| `cros-pd/hoho_v1.7.575-96b74f1.bin` | 65536 | file | `b36777f0a5fb1bbf20c6cdaf781f3ddc8de23aee85e9eb1b842c16a8c5c25ccf` |
| `cros-pd/hoho_v1.7.684-69498dd.bin` | 65536 | file | `61c2fd818df24cc47e2d1667788e35b817ab5136e40dd14e456c38c9fd92a35c` |
| `cros-pd/zinger_v1.7.509-e5bffd3.bin` | 16384 | file | `aaca456178aa845e4e56eb9d10447a888306b11cadc79f4321a1efc9b956be8c` |
| `cros-pd/zinger_v1.7.539-91a0fa2.bin` | 16384 | file | `3f47d486cad28c5a0765ca7f624a0676e2fb4d42679abbda88dc8db72e7f13af` |
| `qcom/sc7180-trogdor/camera/CAMERA_ICP.elf` | 1363812 | file | `1f722d646e0da82f086435002cffcd4e0f890b353ae03f8a37a77ee7714053a5` |
| `qcom/sc7180-trogdor/modem-nolte/mba.mbn` | 283296 | file | `5921570c371c8326686eab3bcdd616aafac31027334169c6fbcf06a91fd1e406` |
| `qcom/sc7180-trogdor/modem-nolte/qdsp6sw.mbn` | 9222444 | file | `821409c327ae9080ef2595e6c403d5acf298bed534fb4f14fe20bebfca39e49b` |
| `qcom/sc7180-trogdor/modem/mba.mbn` | 283296 | file | `38dfe4dc78b4bdc585c3e670c56e4b624e4a804eb21fa52a0b320730e7cd478f` |
| `qcom/sc7180-trogdor/modem/qdsp6sw.mbn` | 65583404 | file | `46ebb2a3734bff4693f0e71e73f66f9e0d3c2e00e7da3d1b70982a2e26e90001` |
| `qcom/venus-5.4/venus.mdt` | — | symlink | `venus.mbn` |
| `rt3070.bin` | — | symlink | `rt2870.bin` |

> Tip: regenerate hashes with `sha256sum` after updating any blob.

