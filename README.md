# Preface #

This document describes the functionality provided by the export policy plugin.

See the [XL Deploy documentation](https://docs.xebialabs.com/) for background information on XL Deploy and deployment concepts.

# CI status #

[![Build Status][xld-export-policy-plugin-travis-image] ][xld-export-policy-plugin-travis-url]
[![Codacy][xld-export-policy-plugin-codacy-image] ][xld-export-policy-plugin-codacy-url]
[![Code Climate][xld-export-policy-plugin-code-climate-image] ][xld-export-policy-plugin-code-climate-url]
[![License: MIT][xld-export-policy-plugin-license-image] ][xld-export-policy-plugin-license-url]
[![Github All Releases][xld-export-policy-plugin-downloads-image] ]()


[xld-export-policy-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-export-policy-plugin.svg?branch=master
[xld-export-policy-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-export-policy-plugin
[xld-export-policy-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/874ac6ffbb2b4639874588ce931b32ad
[xld-export-policy-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xld-export-policy-plugin
[xld-export-policy-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xld-export-policy-plugin/badges/gpa.svg
[xld-export-policy-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xld-export-policy-plugin
[xld-export-policy-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-export-policy-plugin-license-url]: https://opensource.org/licenses/MIT
[xld-export-policy-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xld-export-policy-plugin/total.svg



# Overview #

The XLD export policy plugin is a XL Deploy plugin that adds capability for exporting archived tasks on a policy basis into a `CSV` file. Both Deployment tasks and Control can be exported.

# Requirements #

* **Requirements**
	* **XL Deploy** 5.0.1

# Installation #

Place the plugin xldp file into your `SERVER_HOME/plugins` directory.

# Usage #

1. Go to `Repository - Configuration`, create a new `policy.ExportTaskPolicy`.

The `time pattern` that can be used (not required), can be defined using: http://www.joda.org/joda-time/apidocs/index.html?org/joda/time/format/DateTimeFormat.html
