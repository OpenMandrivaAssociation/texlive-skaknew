# revision 20031
# category Package
# catalog-ctan /fonts/chess/skaknew
# catalog-date 2009-02-21 22:13:29 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-skaknew
Version:	20090221
Release:	1
Summary:	The skak chess fonts redone in Adobe Type 1
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/chess/skaknew
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skaknew.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skaknew.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package offers Adobe Type 1 versions of the fonts provided
as MetaFont source by the skak bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
