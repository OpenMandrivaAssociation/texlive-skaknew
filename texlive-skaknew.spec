%global tl_name skaknew
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The skak chess fonts redone in Adobe Type 1
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/chess/skaknew
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skaknew.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skaknew.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package offers Adobe Type 1 versions of the fonts provided as
Metafont source by the skak bundle.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from skaknew:
Map SkakNew.map
TL_DROPIN_EOF
