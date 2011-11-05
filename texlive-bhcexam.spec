# revision 23304
# category Package
# catalog-ctan /macros/latex/contrib/bhcexam
# catalog-date 2011-07-31 15:37:23 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-bhcexam
Version:	0.2
Release:	1
Summary:	A LaTeX document class specially designed for High School Math Teachers in China
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bhcexam
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A LaTeX document class based on the exam class, which is
specially designed for High School Math Teachers in China.

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
%{_texmfdistdir}/tex/latex/bhcexam/BHCexam.cfg
%{_texmfdistdir}/tex/latex/bhcexam/BHCexam.cls
%doc %{_texmfdistdir}/doc/latex/bhcexam/Makefile
%doc %{_texmfdistdir}/doc/latex/bhcexam/README
%doc %{_texmfdistdir}/doc/latex/bhcexam/test1.tex
%doc %{_texmfdistdir}/doc/latex/bhcexam/test2.tex
%doc %{_texmfdistdir}/doc/latex/bhcexam/test3.tex
%doc %{_texmfdistdir}/doc/latex/bhcexam/test4.tex
#- source
%doc %{_texmfdistdir}/source/latex/bhcexam/BHCexam.dtx
%doc %{_texmfdistdir}/source/latex/bhcexam/BHCexam.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
