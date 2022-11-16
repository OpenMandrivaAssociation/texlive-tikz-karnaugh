Name:		texlive-tikz-karnaugh
Version:	62040
Release:	1
Summary:	Typeset Karnaugh maps using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-karnaugh
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-karnaugh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-karnaugh.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tikz-karnaugh package is a LaTeX package used to draw
Karnaugh maps. It uses TikZ to produce high quality graph from
1 to 12 variables, but this upper limit depends on the TeX
memory usage and can be different for you. It is very good for
presentation since TikZ allows for a better control over the
final appearance of the map. You can control colour, styles and
distances. It can be considered as an upgrade and extension of
Andreas W. Wieland's karnaugh package towards TikZ supporting.
Upgrade because uses TikZ for more option on typesetting and
overall higher quality. Extension because it also supports
American style and inputting the values as they would appear in
the map or in the truth table. Complex maps with solution
(implicants) pointed out can be generated with external java
software (see documentation for details). It supports both
American and traditional (simplified labels) styles and from
version 1.3 on American style is natively supported, therefore,
no more addition work is required to typeset Gray coded labels,
variable names etc. From version 1.4, two new macros allow
typesetting a map much more similarly as it should appear.
Original order, as the values appear in the truth table, still
being supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-karnaugh
%doc %{_texmfdistdir}/doc/latex/tikz-karnaugh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
