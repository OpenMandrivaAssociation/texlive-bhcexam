Name:		texlive-bhcexam
Version:	64093
Release:	1
Summary:	A LaTeX document class designed for High School Math Teachers in China
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bhcexam
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.r64093.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.doc.r64093.tar.xz
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
%{_texmfdistdir}/tex/xelatex/bhcexam
%doc %{_texmfdistdir}/doc/xelatex/bhcexam

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
