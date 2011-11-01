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
Requires(post):	texlive-tlpkg
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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
