# Generated from cucumber-create-meta-6.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-create-meta

Name: rubygem-%{gem_name}
Version: 6.0.1
Release: 1%{?dist}
Summary: cucumber-create-meta-6.0.1
License: MIT
URL: https://github.com/cucumber/create-meta-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
# BuildRequires: rubygem(rspec) >= 3.10
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rspec) >= 3.10.0
BuildArch: noarch

%description
Produce the meta message for Cucumber Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
* Mon Sep 06 2021 Pavel Valena <pvalena@redhat.com> - 6.0.1-1
- Initial package
