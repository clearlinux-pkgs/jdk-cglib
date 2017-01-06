Name     : jdk-cglib
Version  : RELEASE.3.2.4
Release  : 2
URL      : https://github.com/cglib/cglib/archive/RELEASE_3_2_4.tar.gz
Source0  : https://github.com/cglib/cglib/archive/RELEASE_3_2_4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1 Apache-2.0
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-integration-tools
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-sonatype-oss-parent
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
cglib [![Build Status](https://travis-ci.org/cglib/cglib.svg?branch=master)](https://travis-ci.org/cglib/cglib)
================

%prep
%setup -q -n cglib-RELEASE_3_2_4

python3 /usr/share/java-utils/pom_editor.py pom_disable_module cglib-nodep
python3 /usr/share/java-utils/pom_editor.py pom_disable_module cglib-integration-test
python3 /usr/share/java-utils/pom_editor.py pom_disable_module cglib-jmh
python3 /usr/share/java-utils/pom_editor.py pom_xpath_set      pom:packaging 'bundle' cglib
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   pom:build/pom:plugins '<plugin>

                                           <groupId>org.apache.felix</groupId>
                                           <artifactId>maven-bundle-plugin</artifactId>
                                           <version>1.4.0</version>
                                           <extensions>true</extensions>
                                           <configuration>
                                             <instructions>
                                               <Bundle-SymbolicName>net.sf.cglib.core</Bundle-SymbolicName>
                                               <Export-Package>net.*</Export-Package>
                                               <Import-Package>org.apache.tools.*;resolution:=optional,*</Import-Package>
                                             </instructions>
                                           </configuration>
                                         </plugin>' cglib
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  org.apache.maven.plugins:maven-gpg-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  org.apache.maven.plugins:maven-jarsigner-plugin cglib-sample

python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:dependency[pom:artifactId='ant']" "<optional>true</optional>" cglib

python3 /usr/share/java-utils/mvn_alias.py :cglib "net.sf.cglib:cglib" "cglib:cglib-full" "cglib:cglib-nodep" "org.sonatype.sisu.inject:cglib"

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n cglib -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/cglib/cglib-sample.jar
/usr/share/java/cglib/cglib.jar
/usr/share/maven-metadata/cglib.xml
/usr/share/maven-poms/cglib/cglib-parent.pom
/usr/share/maven-poms/cglib/cglib-sample.pom
/usr/share/maven-poms/cglib/cglib.pom
