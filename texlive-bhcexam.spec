%global tl_name bhcexam
%global tl_revision 72638

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	An exam class for mathematics teachers in China
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/bhcexam
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bhcexam.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BHCexam.cls is a LaTeX document class designed for typesetting exams. It
is currently used by the Mathcrowd Problem Database to generate exam PDF
files. The class supports the following features: Support for
configuring whether to display answers. Ability to set whether the
document is formatted in multiple columns. Alignment customization
options. Automatic alignment of option lengths to a grid. Ability to
adjust the width of blank lines based on the length of fill-in-the-blank
answers. Option to display or hide scores for question groups.
Customizable answer space for each question. Ability to restart
numbering in question groups. Support for sub-questions and nested sub-
questions in short-answer questions.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/xelatex
%dir %{_datadir}/texmf-dist/tex/xelatex
%dir %{_datadir}/texmf-dist/doc/xelatex/bhcexam
%dir %{_datadir}/texmf-dist/tex/xelatex/bhcexam
%dir %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/README-zh.md
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/README.md
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples/To7VxKXpZaOWO5Qq9qzeZGtlwYTwJ5KF.jpg
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples/example_student_paper.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples/example_student_paper.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples/example_teacher_paper.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples/example_teacher_paper.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bhcexam/examples/logo.png
%{_datadir}/texmf-dist/tex/xelatex/bhcexam/BHCexam.cls
