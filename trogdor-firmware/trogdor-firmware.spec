Name:           trogdor-firmware
Version:        2025.11.12
Release:        2%{?dist}
Summary:        ChromeOS firmware for trogdor-based Chromebooks

License:        Redistributable, no modification permitted
URL:            https://chromium.googlesource.com/chromiumos/firmware/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       linux-firmware
BuildRequires:  systemd-rpm-macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
This package adds firmware blobs extracted from the ChromeOS strongbad/wormdingler
(trogdor) image. Fedora does not currently ship these files, so they are packaged
here unmodified for compatibility with the Chromebook hardware.

%prep
%setup -q

%build
# Nothing to build.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a usr %{buildroot}/usr

%post
%systemd_post rmtfs-trogdor.service

%preun
%systemd_preun rmtfs-trogdor.service

%postun
%systemd_postun_with_restart rmtfs-trogdor.service

%files
%dir /usr/lib/firmware/cros-pd
/usr/lib/firmware/cros-pd/README.source
/usr/lib/firmware/cros-pd/dingdong_v1.7.317-b0bb7c9.bin
/usr/lib/firmware/cros-pd/dingdong_v1.7.575-96b74f1.bin
/usr/lib/firmware/cros-pd/dingdong_v1.7.684-69498dd.bin
/usr/lib/firmware/cros-pd/hoho_v1.7.317-b0bb7c9.bin
/usr/lib/firmware/cros-pd/hoho_v1.7.575-96b74f1.bin
/usr/lib/firmware/cros-pd/hoho_v1.7.684-69498dd.bin
/usr/lib/firmware/cros-pd/zinger_v1.7.509-e5bffd3.bin
/usr/lib/firmware/cros-pd/zinger_v1.7.539-91a0fa2.bin
%dir /usr/lib/firmware/qcom
%dir /usr/lib/firmware/qcom/sc7180-trogdor
%dir /usr/lib/firmware/qcom/sc7180-trogdor/camera
/usr/lib/firmware/qcom/sc7180-trogdor/camera/CAMERA_ICP.elf
%dir /usr/lib/firmware/qcom/sc7180-trogdor/modem
/usr/lib/firmware/qcom/sc7180-trogdor/modem/mba.mbn
/usr/lib/firmware/qcom/sc7180-trogdor/modem/qdsp6sw.mbn
%dir /usr/lib/firmware/qcom/sc7180-trogdor/modem-nolte
/usr/lib/firmware/qcom/sc7180-trogdor/modem-nolte/mba.mbn
/usr/lib/firmware/qcom/sc7180-trogdor/modem-nolte/qdsp6sw.mbn
%dir /usr/lib/firmware/qcom/venus-5.4
/usr/lib/firmware/qcom/venus-5.4/venus.mdt
/usr/lib/firmware/rt3070.bin
%{_unitdir}/rmtfs-trogdor.service

%changelog
* Wed Nov 12 2025 Craig <craig@example.com> - 2025.11.12-2
- Add rmtfs-trogdor systemd service

* Wed Nov 12 2025 Craig <craig@example.com> - 2025.11.12-1
- Initial package

