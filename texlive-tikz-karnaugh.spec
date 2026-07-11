%global tl_name tikz-karnaugh
%global tl_revision 62040

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Typeset Karnaugh maps using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-karnaugh
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-karnaugh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-karnaugh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tikz-karnaugh package is a LaTeX package used to draw Karnaugh maps.
It uses TikZ to produce high quality graph from 1 to 12 variables, but
this upper limit depends on the TeX memory usage and can be different
for you. It is very good for presentation since TikZ allows for a better
control over the final appearance of the map. You can control colour,
styles and distances. It can be considered as an upgrade and extension
of Andreas W. Wieland's karnaugh package towards TikZ supporting.
Upgrade because uses TikZ for more option on typesetting and overall
higher quality. Extension because it also supports American style and
inputting the values as they would appear in the map or in the truth
table. Complex maps with solution (implicants) pointed out can be
generated with external java software (see documentation for details).
It supports both American and traditional (simplified labels) styles and
from version 1.3 on American style is natively supported, therefore, no
more addition work is required to typeset Gray coded labels, variable
names etc. From version 1.4, two new macros allow typesetting a map much
more similarly as it should appear. Original order, as the values appear
in the truth table, still being supported.

