# Preface #

This document describes the functionality provided by the export policy plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The XLD export policy plugin is a XL Deploy plugin that adds capability for exporting archived tasks on a policy basis into a `CSV` file.

# Requirements #

* **Requirements**
	* **XL Deploy** 5.0.1

# Installation #

Place the plugin xldp file into your `SERVER_HOME/plugins` directory.

# Usage #

1. Go to `Repository - Configuration`, create a new `policy.ExportTaskPolicy`.

The `time pattern` that can be used (not required), can be defined using: http://www.joda.org/joda-time/apidocs/index.html?org/joda/time/format/DateTimeFormat.html
