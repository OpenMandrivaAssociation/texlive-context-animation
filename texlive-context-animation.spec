Name:		texlive-context-animation
Version:	47085
Release:	2
Summary:	Generate fieldstack based animation with ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-animation
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-animation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-animation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a port, to Context (mkvi), of the corresponding
LaTeX package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/context
%{_texmfdistdir}/tex/context/third
%{_texmfdistdir}/tex/context/third/animation
%{_texmfdistdir}/tex/context/third/animation/t-animation.mkvi
%{_texmfdistdir}/tex/context/interface
%{_texmfdistdir}/tex/context/interface/third
%{_texmfdistdir}/tex/context/interface/third/t-animation.xml
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/context
%doc %{_texmfdistdir}/doc/context/third
%doc %{_texmfdistdir}/doc/context/third/animation
%doc %{_texmfdistdir}/doc/context/third/animation/VERSION
%doc %{_texmfdistdir}/doc/context/third/animation/README

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
