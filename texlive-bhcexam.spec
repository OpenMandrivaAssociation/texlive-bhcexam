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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

