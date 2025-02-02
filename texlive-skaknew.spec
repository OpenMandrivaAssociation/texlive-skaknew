Name:		texlive-skaknew
Version:	20031
Release:	2
Summary:	The skak chess fonts redone in Adobe Type 1
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/chess/skaknew
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skaknew.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skaknew.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers Adobe Type 1 versions of the fonts provided
as MetaFont source by the skak bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/skaknew/AlphaDia.afm
%{_texmfdistdir}/fonts/afm/public/skaknew/SkakNew-Diagram.afm
%{_texmfdistdir}/fonts/afm/public/skaknew/SkakNew-DiagramT.afm
%{_texmfdistdir}/fonts/afm/public/skaknew/SkakNew-Figurine.afm
%{_texmfdistdir}/fonts/afm/public/skaknew/SkakNew-FigurineBold.afm
%{_texmfdistdir}/fonts/map/dvips/skaknew/SkakNew.map
%{_texmfdistdir}/fonts/opentype/public/skaknew/AlphaDia.otf
%{_texmfdistdir}/fonts/opentype/public/skaknew/SkakNew-Diagram.otf
%{_texmfdistdir}/fonts/opentype/public/skaknew/SkakNew-DiagramT.otf
%{_texmfdistdir}/fonts/opentype/public/skaknew/SkakNew-Figurine.otf
%{_texmfdistdir}/fonts/opentype/public/skaknew/SkakNew-FigurineBold.otf
%{_texmfdistdir}/fonts/tfm/public/skaknew/AlphaDia.tfm
%{_texmfdistdir}/fonts/tfm/public/skaknew/SkakNew-Diagram.tfm
%{_texmfdistdir}/fonts/tfm/public/skaknew/SkakNew-DiagramT.tfm
%{_texmfdistdir}/fonts/tfm/public/skaknew/SkakNew-Figurine.tfm
%{_texmfdistdir}/fonts/tfm/public/skaknew/SkakNew-FigurineBold.tfm
%{_texmfdistdir}/fonts/type1/public/skaknew/AlphaDia.inf
%{_texmfdistdir}/fonts/type1/public/skaknew/AlphaDia.pfb
%{_texmfdistdir}/fonts/type1/public/skaknew/AlphaDia.pfm
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-Diagram.inf
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-Diagram.pfb
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-Diagram.pfm
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-DiagramT.inf
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-DiagramT.pfb
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-DiagramT.pfm
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-Figurine.inf
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-Figurine.pfb
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-Figurine.pfm
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-FigurineBold.inf
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-FigurineBold.pfb
%{_texmfdistdir}/fonts/type1/public/skaknew/SkakNew-FigurineBold.pfm
%doc %{_texmfdistdir}/doc/fonts/skaknew/README
%doc %{_texmfdistdir}/doc/fonts/skaknew/SkakNew.pdf
%doc %{_texmfdistdir}/doc/fonts/skaknew/SkakNew.tex
%doc %{_texmfdistdir}/doc/fonts/skaknew/fonttables.pdf
%doc %{_texmfdistdir}/doc/fonts/skaknew/install.vtex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
