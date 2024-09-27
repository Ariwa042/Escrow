{pkgs}: {
  deps = [
    pkgs.postgresql_16
    pkgs.cln
    pkgs.tree
    pkgs.python312Packages.django
  ];
}
