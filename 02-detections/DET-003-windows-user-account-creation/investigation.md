# DET-003 — Investigation Guide

## Windows User Account Creation Investigation

---

# 1. Investigation Overview

This document describes the investigation process for DET-003: Windows User Account Creation.

The purpose of this investigation is to demonstrate how a SOC analyst investigates the creation of a Windows user account and determines whether the activity is authorized or potentially malicious.

The detection is triggered when Windows Security Event ID `4720` is generated and matched by the Wazuh custom detection rule.

Unauthorized account creation can be used by attackers to establish persistence, maintain access to a compromised system, or create additional accounts for future activity.

The investigation follows the SOC workflow:

```text
Alert → Triage → Investigate → Correlate → Determine Risk → Respond → Document
