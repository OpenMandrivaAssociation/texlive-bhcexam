# revision 23304
# category Package
# catalog-ctan /macros/latex/contrib/bhcexam
# catalog-date 2011-07-31 15:37:23 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-bhcexam
Version:	0.2
Release:	7
Summary:	A LaTeX document class designed for High School Math Teachers in China
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

%description
A LaTeX document class based on the exam class, which is
specially designed for High School Math Teachers in China.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 749600
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 717914
- texlive-bhcexam
- texlive-bhcexam
- texlive-bhcexam
- texlive-bhcexam
- texlive-bhcexam

