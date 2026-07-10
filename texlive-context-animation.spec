%global tl_name context-animation
%global tl_revision 75386

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Generate fieldstack based animation with ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-animation
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-animation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-animation.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a port, to Context (mkvi), of the corresponding LaTeX
package.

