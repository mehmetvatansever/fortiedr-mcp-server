# FortiEDR API Reference

This file is auto-generated from the official Postman collection.
Regenerate with the `tools/gen_api_reference.py` script.

**Total endpoints:** 146

## Table of Contents

- [api / admin](#api-admin) (2)
- [api / application-control](#api-application-control) (6)
- [api / av-scanner-file-controller](#api-av-scanner-file-controller) (1)
- [api / dashboard](#api-dashboard) (2)
- [api / reputation](#api-reputation) (2)
- [management-rest / admin](#management-rest-admin) (10)
- [management-rest / audit](#management-rest-audit) (1)
- [management-rest / comm-control](#management-rest-comm-control) (8)
- [management-rest / events](#management-rest-events) (7)
- [management-rest / exceptions](#management-rest-exceptions) (5)
- [management-rest / forensics](#management-rest-forensics) (3)
- [management-rest / hash](#management-rest-hash) (1)
- [management-rest / integrations](#management-rest-integrations) (6)
- [management-rest / inventory](#management-rest-inventory) (23)
- [management-rest / iot](#management-rest-iot) (7)
- [management-rest / ip-sets](#management-rest-ip-sets) (4)
- [management-rest / organizations](#management-rest-organizations) (4)
- [management-rest / playbooks-policies](#management-rest-playbooks-policies) (6)
- [management-rest / policies](#management-rest-policies) (7)
- [management-rest / sendable-entities](#management-rest-sendable-entities) (2)
- [management-rest / system-events](#management-rest-system-events) (1)
- [management-rest / threat-hunting](#management-rest-threat-hunting) (15)
- [management-rest / threat-hunting-exclusions](#management-rest-threat-hunting-exclusions) (9)
- [management-rest / threat-hunting-settings](#management-rest-threat-hunting-settings) (6)
- [management-rest / users](#management-rest-users) (8)

---

## api / admin

| Method | Path | Name |
|---|---|---|
| `PUT` | `/api/admin/set-enable-default-application-control-state` | set-enable-default-application-control-state |
| `POST` | `/api/admin/set-tray-notification-settings` | set-tray-notification-settings |

### `PUT` set-enable-default-application-control-state

**Path:** `/api/admin/set-enable-default-application-control-state`

**Body:** JSON body, fields: `isEnableDefaultApplicationControl, organization`

**Description:**

> Update default application control state

---

### `POST` set-tray-notification-settings

**Path:** `/api/admin/set-tray-notification-settings`

**Body:** JSON body, fields: `enabledPopup, enabledTrayNotification, message, organization, enableFortiClientNotification, showNotificationOnFileReadAttempt`

**Description:**

> Update tray notification settings

---

## api / application-control

| Method | Path | Name |
|---|---|---|
| `GET` | `/api/application-control/applications` | applications |
| `POST` | `/api/application-control/applications` | applications |
| `PUT` | `/api/application-control/applications` | applications |
| `DELETE` | `/api/application-control/applications` | applications |
| `POST` | `/api/application-control/force-update-ootb-application-controls` | force-update-ootb-application-controls |
| `POST` | `/api/application-control/tags` | tags |

### `GET` applications

**Path:** `/api/application-control/applications`

**Query params:** `attributes.fileName`, `attributes.path`, `attributes.signer`, `currentPage`, `enabled`, `groupIds`, `groupIds`, `hash`, `operatingSystem`, `organization`, `policyIds`, `policyIds`, `tag`

**Description:**

> Get application controls

---

### `POST` applications

**Path:** `/api/application-control/applications`

**Body:** JSON body, fields: `applicationControls, organization`

**Description:**

> Saves new application controls and returns a list of them

---

### `PUT` applications

**Path:** `/api/application-control/applications`

**Query params:** `appIds`, `appIds`, `organization`

**Body:** JSON body, fields: `groupIds, enabled, isOverridePolicies, name, policyIds, tagId`

**Description:**

> Edits existing application control and returns the affected ones

---

### `DELETE` applications

**Path:** `/api/application-control/applications`

**Query params:** `applicationIds`, `applicationIds`, `organization`

**Description:**

> Deletes application controls

---

### `POST` force-update-ootb-application-controls

**Path:** `/api/application-control/force-update-ootb-application-controls`

**Description:**

> Trigger OOTB application control update

---

### `POST` tags

**Path:** `/api/application-control/tags`

**Body:** JSON body, fields: `name, organization`

**Description:**

> Create an application control tags

---

## api / av-scanner-file-controller

| Method | Path | Name |
|---|---|---|
| `GET` | `/api/av-scanner-file-controller/download` | Stream AV Scanner File |

### `GET` Stream AV Scanner File

**Path:** `/api/av-scanner-file-controller/download`

**Query params:** `version`

**Description:**

> Streams a file from GCS directly to client

---

## api / dashboard

| Method | Path | Name |
|---|---|---|
| `GET` | `/api/dashboard/most-targeted-items` | most-targeted-items |
| `GET` | `/api/dashboard/unhandled-items` | unhandled-items |

### `GET` most-targeted-items

**Path:** `/api/dashboard/most-targeted-items`

**Query params:** `itemType`, `numOfColumns`, `numOfDays`, `organization`

**Description:**

> Returns most targeted devices or most targeted processes, depending on the itemType parameter

---

### `GET` unhandled-items

**Path:** `/api/dashboard/unhandled-items`

**Query params:** `itemType`, `organization`

**Description:**

> Returns unhandled devices or unhandled processes, depending on the itemType parameter

---

## api / reputation

| Method | Path | Name |
|---|---|---|
| `GET` | `/api/reputation/regions` | regions |
| `PUT` | `/api/reputation/regions` | regions |

### `GET` regions

**Path:** `/api/reputation/regions`

**Query params:** `organizationId`

**Description:**

> retrieves reputation region entity

---

### `PUT` regions

**Path:** `/api/reputation/regions`

**Query params:** `organizationId`

**Body:** JSON array (2 sample records)

**Description:**

> select regions for specific organization

---

## management-rest / admin

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/admin/list-collector-installers` | list-collector-installers |
| `GET` | `/management-rest/admin/list-system-summary` | list-system-summary |
| `DELETE` | `/management-rest/admin/previous-registration-passwords/:passwordId` | previous-registration-passwords |
| `GET` | `/management-rest/admin/previous-registration-passwords` | previous-registration-passwords |
| `GET` | `/management-rest/admin/ready` | ready |
| `POST` | `/management-rest/admin/registration-password` | registration-password |
| `PUT` | `/management-rest/admin/set-system-mode` | set-system-mode |
| `POST` | `/management-rest/admin/update-collector-installer` | update-collector-installer |
| `POST` | `/management-rest/admin/upload-content` | upload-content |
| `PUT` | `/management-rest/admin/upload-license` | upload-license |

### `GET` list-collector-installers

**Path:** `/management-rest/admin/list-collector-installers`

**Query params:** `organization`

**Description:**

> This API call output the available collectors installers

---

### `GET` list-system-summary

**Path:** `/management-rest/admin/list-system-summary`

**Query params:** `addLicenseBlob`, `organization`

**Description:**

> Get System Summary

---

### `DELETE` previous-registration-passwords

**Path:** `/management-rest/admin/previous-registration-passwords/:passwordId`

**Body:** JSON body, fields: `organization`

**Description:**

> This API deletes previous registration password for given id

---

### `GET` previous-registration-passwords

**Path:** `/management-rest/admin/previous-registration-passwords`

**Body:** JSON body, fields: `organization`

**Description:**

> This API retrieve previous registration passwords for given organization

---

### `GET` ready

**Path:** `/management-rest/admin/ready`

**Description:**

> Get System Readiness

---

### `POST` registration-password

**Path:** `/management-rest/admin/registration-password`

**Body:** JSON body, fields: `organization, password`

**Description:**

> This API creates new registration password for given organization

---

### `PUT` set-system-mode

**Path:** `/management-rest/admin/set-system-mode`

**Query params:** `forceAll`, `mode`, `organization`

**Description:**

> Set system modeThis API call enables you to switch the system to Simulation mode

---

### `POST` update-collector-installer

**Path:** `/management-rest/admin/update-collector-installer`

**Query params:** `collectorGroupIds`, `collectorGroupIds`, `collectorGroups`, `collectorGroups`, `organization`

**Body:** JSON body, fields: `updateVersions`

**Description:**

> This API update collectors target version for collector groups

---

### `POST` upload-content

**Path:** `/management-rest/admin/upload-content`

**Body:** form-data: file

**Description:**

> Upload content to the system

---

### `PUT` upload-license

**Path:** `/management-rest/admin/upload-license`

**Body:** JSON body, fields: `licenseBlob`

**Description:**

> Upload license to the system

---

## management-rest / audit

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/audit/get-audit` | get-audit |

### `GET` get-audit

**Path:** `/management-rest/audit/get-audit`

**Query params:** `fromTime`, `organization`, `toTime`

**Description:**

> This API retrieve the audit between 2 dates

---

## management-rest / comm-control

| Method | Path | Name |
|---|---|---|
| `PUT` | `/management-rest/comm-control/assign-collector-group` | assign-collector-group |
| `POST` | `/management-rest/comm-control/clone-policy` | clone-policy |
| `GET` | `/management-rest/comm-control/list-policies` | list-policies |
| `GET` | `/management-rest/comm-control/list-products` | list-products |
| `PUT` | `/management-rest/comm-control/resolve-applications` | resolve-applications |
| `PUT` | `/management-rest/comm-control/set-policy-mode` | set-policy-mode |
| `PUT` | `/management-rest/comm-control/set-policy-permission` | set-policy-permission |
| `PUT` | `/management-rest/comm-control/set-policy-rule-state` | set-policy-rule-state |

### `PUT` assign-collector-group

**Path:** `/management-rest/comm-control/assign-collector-group`

**Query params:** `collectorGroups`, `collectorGroups`, `forceAssign`, `organization`, `policyName`

**Description:**

> Assign collector group to application policy

---

### `POST` clone-policy

**Path:** `/management-rest/comm-control/clone-policy`

**Query params:** `newPolicyName`, `organization`, `sourcePolicyName`

**Description:**

> application clone policy

---

### `GET` list-policies

**Path:** `/management-rest/comm-control/list-policies`

**Query params:** `decisions`, `itemsPerPage`, `organization`, `pageNumber`, `policies`, `policies`, `rules`, `rules`, `sorting`, `sources`, `state`, `strictMode`

**Description:**

> This API call outputs a list of all the communication control policies in the system, and information about each of them

---

### `GET` list-products

**Path:** `/management-rest/comm-control/list-products`

**Query params:** `action`, `collectorGroups`, `collectorGroups`, `cveIdentifier`, `destinationIp`, `destinationIp`, `devices`, `devices`, `firstConnectionTimeEnd`, `firstConnectionTimeStart`, `handled`, `includeStatistics`, `ips`, `ips`, `itemsPerPage`, `lastConnectionTimeEnd`, `lastConnectionTimeStart`, `organization`, `os`, `pageNumber`, `policies`, `policies`, `processHash`, `processes`, `processes`, `product`, `products`, `products`, `reputation`, `reputation`, `rule`, `rulePolicy`, `seen`, `sorting`, `strictMode`, `vendor`, `vendors`, `vendors`, `version`, `versions`, `versions`, `vulnerabilities`

**Description:**

> This API call outputs a list of all the communicating applications in the system, and information about each of them

---

### `PUT` resolve-applications

**Path:** `/management-rest/comm-control/resolve-applications`

**Query params:** `applyNested`, `comment`, `organization`, `products`, `products`, `resolve`, `signed`, `vendors`, `vendors`, `versions`, `versions`

**Description:**

> Enable resolving/unresolving applications

---

### `PUT` set-policy-mode

**Path:** `/management-rest/comm-control/set-policy-mode`

**Query params:** `mode`, `organization`, `policyNames`, `policyNames`

**Description:**

> Set policy to simulation/prevention

---

### `PUT` set-policy-permission

**Path:** `/management-rest/comm-control/set-policy-permission`

**Query params:** `applyNested`, `decision`, `organization`, `policies`, `policies`, `products`, `products`, `signed`, `vendors`, `vendors`, `versions`, `versions`

**Description:**

> Set the application allow/deny

---

### `PUT` set-policy-rule-state

**Path:** `/management-rest/comm-control/set-policy-rule-state`

**Query params:** `organization`, `policyName`, `ruleName`, `state`

**Description:**

> Set rule in policy to enable/disable

---

## management-rest / events

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/events/count-events` | count-events |
| `POST` | `/management-rest/events/create-exception` | create-exception |
| `GET` | `/management-rest/events/export-raw-data-items-json` | export-raw-data-items-json |
| `GET` | `/management-rest/events/list-events` | list-events |
| `GET` | `/management-rest/events/list-raw-data-items` | list-raw-data-items |
| `PUT` | `/management-rest/events` | events |
| `DELETE` | `/management-rest/events` | events |

### `GET` count-events

**Path:** `/management-rest/events/count-events`

**Query params:** `actions`, `applicationControl`, `archived`, `classifications`, `collectorGroups`, `collectorGroups`, `collectorIds`, `collectorIds`, `destinations`, `destinations`, `device`, `deviceControl`, `deviceIps`, `deviceIps`, `eventIds`, `eventIds`, `eventType`, `expired`, `fileHash`, `firstSeen`, `firstSeenFrom`, `firstSeenTo`, `handled`, `itemsPerPage`, `lastSeen`, `lastSeenFrom`, `lastSeenTo`, `loggedUser`, `macAddresses`, `macAddresses`, `muted`, `operatingSystems`, `operatingSystems`, `organization`, `pageNumber`, `paths`, `paths`, `process`, `rule`, `seen`, `severities`, `signed`, `sorting`, `strictMode`

**Description:**

> Count Events

---

### `POST` create-exception

**Path:** `/management-rest/events/create-exception`

**Query params:** `allCollectorGroups`, `allDestinations`, `allOrganizations`, `allUsers`, `collectorGroups`, `collectorGroups`, `comment`, `destinations`, `destinations`, `eventId`, `exceptionId`, `forceCreate`, `isHidden`, `organization`, `users`, `users`

**Body:** JSON body, fields: `useAnyPath, useCommandLine, useInException, wildcardFiles, wildcardPaths`

**Description:**

> This API call adds an exception to a specific event. The output of this call is a message indicating whether the creation of the exception

---

### `GET` export-raw-data-items-json

**Path:** `/management-rest/events/export-raw-data-items-json`

**Query params:** `organization`, `rawItemIds`

**Description:**

> Get event as Json format

---

### `GET` list-events

**Path:** `/management-rest/events/list-events`

**Query params:** `actions`, `applicationControl`, `archived`, `classifications`, `collectorGroups`, `collectorGroups`, `collectorIds`, `collectorIds`, `destinations`, `destinations`, `device`, `deviceControl`, `deviceIps`, `deviceIps`, `eventIds`, `eventIds`, `eventType`, `expired`, `fileHash`, `firstSeen`, `firstSeenFrom`, `firstSeenTo`, `handled`, `itemsPerPage`, `lastSeen`, `lastSeenFrom`, `lastSeenTo`, `loggedUser`, `macAddresses`, `macAddresses`, `muted`, `operatingSystems`, `operatingSystems`, `organization`, `pageNumber`, `paths`, `paths`, `process`, `rule`, `seen`, `severities`, `signed`, `sorting`, `strictMode`, `allCollectorGroups`, `allDestinations`, `allUsers`, `forceCreate`, `comment`, `eventId`, `organization`

**Description:**

> List Events

---

### `GET` list-raw-data-items

**Path:** `/management-rest/events/list-raw-data-items`

**Query params:** `collectorGroups`, `collectorGroups`, `destinations`, `destinations`, `device`, `deviceIps`, `deviceIps`, `eventId`, `firstSeen`, `firstSeenFrom`, `firstSeenTo`, `fullDataRequested`, `itemsPerPage`, `lastSeen`, `lastSeenFrom`, `lastSeenTo`, `loggedUser`, `organization`, `pageNumber`, `rawEventIds`, `rawEventIds`, `sorting`, `strictMode`

**Description:**

> List raw data items

---

### `PUT` events

**Path:** `/management-rest/events`

**Query params:** `actions`, `applicationControl`, `archived`, `classifications`, `collectorGroups`, `collectorGroups`, `collectorIds`, `collectorIds`, `destinations`, `destinations`, `device`, `deviceControl`, `deviceIps`, `deviceIps`, `eventIds`, `eventType`, `expired`, `fileHash`, `firstSeen`, `firstSeenFrom`, `firstSeenTo`, `handled`, `itemsPerPage`, `lastSeen`, `lastSeenFrom`, `lastSeenTo`, `loggedUser`, `macAddresses`, `macAddresses`, `muted`, `operatingSystems`, `operatingSystems`, `organization`, `pageNumber`, `paths`, `paths`, `process`, `rule`, `seen`, `severities`, `signed`, `sorting`, `strictMode`, `eventId`

**Body:** JSON body, fields: `archive, classification, comment, familyName, forceUnmute, handle, malwareType, mute, muteDuration, read, threatName`

**Description:**

> This API call updates the read/unread, handled/unhandled or archived/unarchived state of an event. The output of this call is a message indicating whether the update succeeded or failed

---

### `DELETE` events

**Path:** `/management-rest/events`

**Query params:** `actions`, `applicationControl`, `archived`, `classifications`, `collectorGroups`, `collectorGroups`, `collectorIds`, `collectorIds`, `deleteAll`, `destinations`, `destinations`, `device`, `deviceControl`, `deviceIps`, `deviceIps`, `eventIds`, `eventIds`, `eventType`, `expired`, `fileHash`, `firstSeen`, `firstSeenFrom`, `firstSeenTo`, `handled`, `itemsPerPage`, `lastSeen`, `lastSeenFrom`, `lastSeenTo`, `loggedUser`, `macAddresses`, `macAddresses`, `muted`, `operatingSystems`, `operatingSystems`, `organization`, `pageNumber`, `paths`, `paths`, `process`, `rule`, `seen`, `severities`, `signed`, `sorting`, `strictMode`

**Description:**

> This API call delete events

---

## management-rest / exceptions

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/exceptions/create-or-edit-exception` | create-or-edit-exception |
| `DELETE` | `/management-rest/exceptions/delete` | delete |
| `GET` | `/management-rest/exceptions/get-event-exceptions` | get-event-exceptions |
| `GET` | `/management-rest/exceptions/list-exceptions` | list-exceptions |
| `POST` | `/management-rest/exceptions/update-exceptions-to-all-accounts-groups-coverage` | update-exceptions-to-all-accounts-groups-coverage |

### `POST` create-or-edit-exception

**Path:** `/management-rest/exceptions/create-or-edit-exception`

**Query params:** `confirmEdit`, `organization`

**Body:** Raw body (6 chars)

**Description:**

> This API call creates a new exception or updates an existing exception based on the given exception JSON body parameter

---

### `DELETE` delete

**Path:** `/management-rest/exceptions/delete`

**Query params:** `collectorGroups`, `collectorGroups`, `comment`, `createdAfter`, `createdBefore`, `deleteAll`, `destination`, `exceptionId`, `exceptionIds`, `exceptionIds`, `organization`, `path`, `process`, `rules`, `rules`, `updatedAfter`, `updatedBefore`, `user`

**Description:**

> Delete exceptions

---

### `GET` get-event-exceptions

**Path:** `/management-rest/exceptions/get-event-exceptions`

**Query params:** `eventId`, `organization`

**Description:**

> Show exceptions

---

### `GET` list-exceptions

**Path:** `/management-rest/exceptions/list-exceptions`

**Query params:** `collectorGroups`, `collectorGroups`, `comment`, `createdAfter`, `createdBefore`, `destination`, `exceptionIds`, `exceptionIds`, `organization`, `path`, `process`, `rules`, `rules`, `updatedAfter`, `updatedBefore`, `user`

**Description:**

> List of exceptions

---

### `POST` update-exceptions-to-all-accounts-groups-coverage

**Path:** `/management-rest/exceptions/update-exceptions-to-all-accounts-groups-coverage`

**Query params:** `organization`

**Description:**

> This API call set an exception to a 'All organizations agents groups'

---

## management-rest / forensics

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/forensics/get-event-file` | get-event-file |
| `GET` | `/management-rest/forensics/get-file` | get-file |
| `PUT` | `/management-rest/forensics/remediate-device` | remediate-device |

### `GET` get-event-file

**Path:** `/management-rest/forensics/get-event-file`

**Query params:** `disk`, `endRange`, `filePaths`, `filePaths`, `memory`, `organization`, `processId`, `rawEventId`, `startRange`

**Description:**

> This API call retrieves a file or memory

---

### `GET` get-file

**Path:** `/management-rest/forensics/get-file`

**Query params:** `device`, `filePaths`, `filePaths`, `organization`, `type`

**Description:**

> This API call retrieves a file or memory

---

### `PUT` remediate-device

**Path:** `/management-rest/forensics/remediate-device`

**Query params:** `device`, `deviceId`, `executablesToRemove`, `executablesToRemove`, `organization`, `persistenceDataAction`, `persistenceDataNewContent`, `persistenceDataPath`, `persistenceDataValueName`, `persistenceDataValueNewType`, `processName`, `terminatedProcessId`, `threadId`

**Description:**

> This API kill process / delete file / clean persistence, File and persistence paths must be specified in a logical format

---

## management-rest / hash

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/hash/search` | search |

### `GET` search

**Path:** `/management-rest/hash/search`

**Query params:** `fileHashes`, `fileHashes`, `organization`

**Description:**

> This API enables the user to search a file hash among the current events, threat hunting repository and communicating applications that exist in the system

---

## management-rest / integrations

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/integrations/connectors-metadata` | connectors-metadata |
| `POST` | `/management-rest/integrations/create-connector` | create-connector |
| `DELETE` | `/management-rest/integrations/delete-connector` | delete-connector |
| `GET` | `/management-rest/integrations/list-connectors` | list-connectors |
| `GET` | `/management-rest/integrations/test-connector` | test-connector |
| `PUT` | `/management-rest/integrations/update-connector` | update-connector |

### `GET` connectors-metadata

**Path:** `/management-rest/integrations/connectors-metadata`

**Query params:** `organization`

**Description:**

> Get connectors metadata, describing the valid values for connector fields definition and on-premise cores.

---

### `POST` create-connector

**Path:** `/management-rest/integrations/create-connector`

**Body:** JSON body, fields: `connectorActions, enabled, host, name, organization, port, type, vendor, apiKey, coreId, password, username`

**Description:**

> Creates a new connector. Please note: Creation of Custom connectors/actions is not yet support.

---

### `DELETE` delete-connector

**Path:** `/management-rest/integrations/delete-connector`

**Query params:** `connectorName`, `connectorType`, `organization`

**Description:**

> Deletes a connector

---

### `GET` list-connectors

**Path:** `/management-rest/integrations/list-connectors`

**Query params:** `onlyValidConnectors`, `organization`

**Description:**

> List all organization connectors

---

### `GET` test-connector

**Path:** `/management-rest/integrations/test-connector`

**Query params:** `connectorName`, `connectorType`, `organization`

**Description:**

> Tests a connector

---

### `PUT` update-connector

**Path:** `/management-rest/integrations/update-connector`

**Body:** JSON body, fields: `connectorActions, enabled, host, name, organization, port, type, vendor, apiKey, coreId, password, username`

**Description:**

> Updates an existing connector based on (name, type, organization). Please note: Modification of Custom connectors/actions is not yet support.

---

## management-rest / inventory

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/inventory/aggregator-logs` | aggregator-logs |
| `GET` | `/management-rest/inventory/check-custom-installer` | check-custom-installer |
| `GET` | `/management-rest/inventory/collector-logs` | collector-logs |
| `GET` | `/management-rest/inventory/core-logs` | core-logs |
| `POST` | `/management-rest/inventory/create-collector-group` | create-collector-group |
| `POST` | `/management-rest/inventory/create-ems-custom-installer` | create-ems-custom-installer |
| `DELETE` | `/management-rest/inventory/delete-collectors` | delete-collectors |
| `PUT` | `/management-rest/inventory/ems-move-collectors` | ems-move-collectors |
| `PUT` | `/management-rest/inventory/isolate-collectors` | isolate-collectors |
| `GET` | `/management-rest/inventory/list-aggregators` | list-aggregators |
| `GET` | `/management-rest/inventory/list-collector-groups` | list-collector-groups |
| `GET` | `/management-rest/inventory/list-collectors` | list-collectors |
| `GET` | `/management-rest/inventory/list-cores` | list-cores |
| `GET` | `/management-rest/inventory/list-repositories` | list-repositories |
| `GET` | `/management-rest/inventory/list-unmanaged-devices` | list-unmanaged-devices |
| `PUT` | `/management-rest/inventory/move-collectors` | move-collectors |
| `POST` | `/management-rest/inventory/moveCollectorsToAnotherAggregator` | moveCollectorsToAnotherAggregator |
| `PUT` | `/management-rest/inventory/release-license` | release-license |
| `GET` | `/management-rest/inventory/system-logs` | system-logs |
| `PUT` | `/management-rest/inventory/toggle-collectors` | toggle-collectors |
| `POST` | `/management-rest/inventory/uninstall-collectors` | uninstall-collectors |
| `PUT` | `/management-rest/inventory/unisolate-collectors` | unisolate-collectors |
| `PUT` | `/management-rest/inventory/update-collector-group-name` | update-collector-group-name |

### `GET` aggregator-logs

**Path:** `/management-rest/inventory/aggregator-logs`

**Query params:** `device`, `deviceId`, `organization`

**Description:**

> This API call retrieves a aggregator logs

---

### `GET` check-custom-installer

**Path:** `/management-rest/inventory/check-custom-installer`

**Query params:** `customInstallerID`

**Description:**

> This API call for checking the results for an custom installer request and getting the installer url

---

### `GET` collector-logs

**Path:** `/management-rest/inventory/collector-logs`

**Query params:** `device`, `deviceId`, `organization`

**Description:**

> This API call retrieves a collector logs

---

### `GET` core-logs

**Path:** `/management-rest/inventory/core-logs`

**Query params:** `device`, `deviceId`, `organization`

**Description:**

> This API call retrieves a core logs

---

### `POST` create-collector-group

**Path:** `/management-rest/inventory/create-collector-group`

**Query params:** `name`, `organization`

**Description:**

> This API call create collector group

---

### `POST` create-ems-custom-installer

**Path:** `/management-rest/inventory/create-ems-custom-installer`

**Query params:** `aggregatorAddress`, `aggregatorPort`, `citrixPVS`, `collectorGroup`, `collectorVersion`, `distro`, `is64bit`, `organization`, `osType`, `proxy`, `vdi`

**Description:**

> This API call sends request for creating custom-installer for EMS integration

---

### `DELETE` delete-collectors

**Path:** `/management-rest/inventory/delete-collectors`

**Query params:** `cloudAccounts`, `cloudAccounts`, `cloudProviders`, `cloudProviders`, `clusters`, `clusters`, `collectorGroups`, `collectorGroups`, `collectorGroupsIds`, `collectorGroupsIds`, `collectorType`, `confirmDeletion`, `deleteAll`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeen`, `hasCrashDumps`, `ips`, `ips`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `loggedUser`, `operatingSystems`, `operatingSystems`, `organization`, `osFamilies`, `osFamilies`, `pageNumber`, `showExpired`, `sorting`, `states`, `strictMode`, `versions`, `versions`

**Description:**

> This API call deletes a Collector(s)

---

### `PUT` ems-move-collectors

**Path:** `/management-rest/inventory/ems-move-collectors`

**Query params:** `collectorIds`, `collectorIds`, `collectorSIDs`, `collectorSIDs`, `collectors`, `collectors`, `forceAssign`, `organization`, `targetCollectorGroup`

**Description:**

> This API call move collector between groups for EMS integration

---

### `PUT` isolate-collectors

**Path:** `/management-rest/inventory/isolate-collectors`

**Query params:** `devices`, `devices`, `devicesIds`, `devicesIds`, `organization`

**Description:**

> This API call isolate collector functionality

---

### `GET` list-aggregators

**Path:** `/management-rest/inventory/list-aggregators`

**Query params:** `ip`, `names`, `names`, `organization`, `versions`, `versions`

**Description:**

> This API call output the list of aggregators

---

### `GET` list-collector-groups

**Path:** `/management-rest/inventory/list-collector-groups`

**Query params:** `organization`

**Description:**

> This API call output the collectors groups

---

### `GET` list-collectors

**Path:** `/management-rest/inventory/list-collectors`

**Query params:** `cloudAccounts`, `cloudAccounts`, `cloudProviders`, `cloudProviders`, `clusters`, `clusters`, `collectorGroups`, `collectorGroups`, `collectorGroupsIds`, `collectorGroupsIds`, `collectorType`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeen`, `hasCrashDumps`, `ips`, `ips`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `loggedUser`, `operatingSystems`, `operatingSystems`, `organization`, `osFamilies`, `osFamilies`, `pageNumber`, `showExpired`, `sorting`, `states`, `strictMode`, `versions`, `versions`

**Description:**

> This API call outputs a list of the Collectors in the system. Use the input parameters to filter the list

---

### `GET` list-cores

**Path:** `/management-rest/inventory/list-cores`

**Query params:** `deploymentModes`, `deploymentModes`, `hasCrashDumps`, `ip`, `names`, `names`, `organization`, `versions`, `versions`

**Description:**

> This API call output the list of cores

---

### `GET` list-repositories

**Path:** `/management-rest/inventory/list-repositories`

**Description:**

> This API call output the list of repositories (edrs)

---

### `GET` list-unmanaged-devices

**Path:** `/management-rest/inventory/list-unmanaged-devices`

**Query params:** `itemsPerPage`, `organization`, `pageNumber`, `sorting`, `strictMode`

**Description:**

> This API call outputs a list of the unmanaged devices in the system

---

### `PUT` move-collectors

**Path:** `/management-rest/inventory/move-collectors`

**Query params:** `collectorIds`, `collectorIds`, `collectorSIDs`, `collectorSIDs`, `collectors`, `collectors`, `forceAssign`, `organization`, `targetCollectorGroup`

**Description:**

> This API call move collector between groups

---

### `POST` moveCollectorsToAnotherAggregator

**Path:** `/management-rest/inventory/moveCollectorsToAnotherAggregator`

**Query params:** `address`, `cloudAccounts`, `cloudAccounts`, `cloudProviders`, `cloudProviders`, `clusters`, `clusters`, `collectorGroups`, `collectorGroups`, `collectorGroupsIds`, `collectorGroupsIds`, `collectorType`, `destinationAccountName`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeen`, `hasCrashDumps`, `ips`, `ips`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `loggedUser`, `operatingSystems`, `operatingSystems`, `organization`, `osFamilies`, `osFamilies`, `pageNumber`, `showExpired`, `sorting`, `states`, `strictMode`, `versions`, `versions`

**Description:**

> This API call starts collectors transfer to another aggregator. Use the input parameters to filter the list

---

### `PUT` release-license

**Path:** `/management-rest/inventory/release-license`

**Query params:** `cloudAccounts`, `cloudAccounts`, `cloudProviders`, `cloudProviders`, `clusters`, `clusters`, `collectorGroups`, `collectorGroups`, `collectorGroupsIds`, `collectorGroupsIds`, `collectorType`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeen`, `hasCrashDumps`, `ips`, `ips`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `loggedUser`, `operatingSystems`, `operatingSystems`, `organization`, `osFamilies`, `osFamilies`, `pageNumber`, `releaseLicense`, `showExpired`, `sorting`, `states`, `strictMode`, `versions`, `versions`

**Description:**

> This API call enables/disables a Collector(s) and release it license. You must specify whether the License must be released or acquired! Cooldown between the requests should be 2-3 minutes!

---

### `GET` system-logs

**Path:** `/management-rest/inventory/system-logs`

**Description:**

> This API call retrieves a system logs

---

### `PUT` toggle-collectors

**Path:** `/management-rest/inventory/toggle-collectors`

**Query params:** `cloudAccounts`, `cloudAccounts`, `cloudProviders`, `cloudProviders`, `clusters`, `clusters`, `collectorGroups`, `collectorGroups`, `collectorGroupsIds`, `collectorGroupsIds`, `collectorType`, `devices`, `devices`, `devicesIds`, `devicesIds`, `enable`, `firstSeen`, `hasCrashDumps`, `ips`, `ips`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `loggedUser`, `operatingSystems`, `operatingSystems`, `organization`, `osFamilies`, `osFamilies`, `pageNumber`, `showExpired`, `sorting`, `states`, `strictMode`, `versions`, `versions`

**Description:**

> This API call enables/disables a Collector(s). You must specify whether the Collector is to be enabled or disabled

---

### `POST` uninstall-collectors

**Path:** `/management-rest/inventory/uninstall-collectors`

**Query params:** `collectorIDs`, `collectorIDs`, `collectorSIDs`, `collectorSIDs`, `organization`

**Description:**

> This API uninstall collectors

---

### `PUT` unisolate-collectors

**Path:** `/management-rest/inventory/unisolate-collectors`

**Query params:** `devices`, `devices`, `devicesIds`, `devicesIds`, `organization`

**Description:**

> This API call isolate collector functionality

---

### `PUT` update-collector-group-name

**Path:** `/management-rest/inventory/update-collector-group-name`

**Query params:** `collectorGroupId`, `groupName`

**Description:**

> This API updates collector group name!

---

## management-rest / iot

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/iot/create-iot-group` | create-iot-group |
| `DELETE` | `/management-rest/iot/delete-devices` | delete-devices |
| `GET` | `/management-rest/iot/export-iot-json` | export-iot-json |
| `GET` | `/management-rest/iot/list-iot-devices` | list-iot-devices |
| `GET` | `/management-rest/iot/list-iot-groups` | list-iot-groups |
| `PUT` | `/management-rest/iot/move-iot-devices` | move-iot-devices |
| `PUT` | `/management-rest/iot/rescan-iot-device-details` | rescan-iot-device-details |

### `POST` create-iot-group

**Path:** `/management-rest/iot/create-iot-group`

**Query params:** `name`, `organization`

**Description:**

> This API call create IoT group

---

### `DELETE` delete-devices

**Path:** `/management-rest/iot/delete-devices`

**Query params:** `categories`, `categories`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeenEnd`, `firstSeenStart`, `internalIps`, `internalIps`, `iotGroups`, `iotGroups`, `iotGroupsIds`, `iotGroupsIds`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `locations`, `locations`, `macAddresses`, `macAddresses`, `models`, `models`, `organization`, `pageNumber`, `showExpired`, `sorting`, `strictMode`, `vendors`, `vendors`

**Description:**

> This API call deletes a IoT device(s)

---

### `GET` export-iot-json

**Path:** `/management-rest/iot/export-iot-json`

**Query params:** `iotDeviceIds`, `iotDeviceIds`, `organization`

**Description:**

> This API call outputs a list of the IoT devices info

---

### `GET` list-iot-devices

**Path:** `/management-rest/iot/list-iot-devices`

**Query params:** `categories`, `categories`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeenEnd`, `firstSeenStart`, `internalIps`, `internalIps`, `iotGroups`, `iotGroups`, `iotGroupsIds`, `iotGroupsIds`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `locations`, `locations`, `macAddresses`, `macAddresses`, `models`, `models`, `organization`, `pageNumber`, `showExpired`, `sorting`, `strictMode`, `vendors`, `vendors`

**Description:**

> This API call outputs a list of the IoT devices in the system. Use the input parameters to filter the list

---

### `GET` list-iot-groups

**Path:** `/management-rest/iot/list-iot-groups`

**Query params:** `organization`

**Description:**

> This API call output the IoT devices groups

---

### `PUT` move-iot-devices

**Path:** `/management-rest/iot/move-iot-devices`

**Query params:** `iotDeviceIds`, `iotDeviceIds`, `organization`, `targetIotGroup`

**Description:**

> This API call move IoT devices between groups

---

### `PUT` rescan-iot-device-details

**Path:** `/management-rest/iot/rescan-iot-device-details`

**Query params:** `categories`, `categories`, `devices`, `devices`, `devicesIds`, `devicesIds`, `firstSeenEnd`, `firstSeenStart`, `internalIps`, `internalIps`, `iotGroups`, `iotGroups`, `iotGroupsIds`, `iotGroupsIds`, `itemsPerPage`, `lastSeenEnd`, `lastSeenStart`, `locations`, `locations`, `macAddresses`, `macAddresses`, `models`, `models`, `organization`, `pageNumber`, `showExpired`, `sorting`, `strictMode`, `vendors`, `vendors`

**Description:**

> This API call device details scan on IoT device(s)

---

## management-rest / ip-sets

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/ip-sets/create-ip-set` | create-ip-set |
| `DELETE` | `/management-rest/ip-sets/delete-ip-set` | delete-ip-set |
| `GET` | `/management-rest/ip-sets/list-ip-sets` | list-ip-sets |
| `PUT` | `/management-rest/ip-sets/update-ip-set` | update-ip-set |

### `POST` create-ip-set

**Path:** `/management-rest/ip-sets/create-ip-set`

**Body:** JSON body, fields: `include, name, description, exclude, organization`

**Description:**

> This API create IP sets in the system.
> Use the input parameter organization=All organizations to create for all the organization. (only for Admin role

---

### `DELETE` delete-ip-set

**Path:** `/management-rest/ip-sets/delete-ip-set`

**Query params:** `ipSets`, `ipSets`, `organization`

**Description:**

> This API delete IP sets from the system. Use the input parameters to filter organization

---

### `GET` list-ip-sets

**Path:** `/management-rest/ip-sets/list-ip-sets`

**Query params:** `ip`, `organization`

**Description:**

> This API call outputs a list of the IP sets in the system. Use the input parameters to filter the list

---

### `PUT` update-ip-set

**Path:** `/management-rest/ip-sets/update-ip-set`

**Query params:** `organization`

**Body:** JSON body, fields: `include, name, description, exclude`

**Description:**

> This API update IP sets in the system. Use the input parameters to filter organization

---

## management-rest / organizations

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/organizations/create-organization` | create-organization |
| `DELETE` | `/management-rest/organizations/delete-organization` | delete-organization |
| `GET` | `/management-rest/organizations/list-organizations` | list-organizations |
| `PUT` | `/management-rest/organizations/update-organization` | update-organization |

### `POST` create-organization

**Path:** `/management-rest/organizations/create-organization`

**Body:** JSON body, fields: `expirationDate, name, password, passwordConfirmation, eXtendedDetection, edr, edrAddOnsAllocated, edrBackupEnabled, edrEnabled, edrNumberOfShards, edrStorageAllocatedInMb, endpointsAllocated, forensics, iotAllocated, requestPolicyEngineLibUpdates`...

**Description:**

> This API creates organization in the system (only for Admin role)

---

### `DELETE` delete-organization

**Path:** `/management-rest/organizations/delete-organization`

**Query params:** `organization`

**Description:**

> This API delete organization in the system (only for Admin role)

---

### `GET` list-organizations

**Path:** `/management-rest/organizations/list-organizations`

**Description:**

> This API call outputs a list of the accounts in the system.

---

### `PUT` update-organization

**Path:** `/management-rest/organizations/update-organization`

**Query params:** `organization`

**Body:** JSON body, fields: `eXtendedDetection, edr, edrAddOnsAllocated, edrBackupEnabled, edrEnabled, edrNumberOfShards, edrStorageAllocatedInMb, endpointsAllocated, expirationDate, forensics, iotAllocated, name, requestPolicyEngineLibUpdates, serialNumber, serversAllocated`...

**Description:**

> This API update organization in the system (only for Admin role)

---

## management-rest / playbooks-policies

| Method | Path | Name |
|---|---|---|
| `PUT` | `/management-rest/playbooks-policies/assign-collector-group` | assign-collector-group |
| `POST` | `/management-rest/playbooks-policies/clone` | clone |
| `GET` | `/management-rest/playbooks-policies/list-policies` | list-policies |
| `PUT` | `/management-rest/playbooks-policies/map-connectors-to-actions` | map-connectors-to-actions |
| `PUT` | `/management-rest/playbooks-policies/set-action-classification` | set-action-classification |
| `PUT` | `/management-rest/playbooks-policies/set-mode` | set-mode |

### `PUT` assign-collector-group

**Path:** `/management-rest/playbooks-policies/assign-collector-group`

**Query params:** `collectorGroupNames`, `collectorGroupNames`, `forceAssign`, `organization`, `policyName`

**Description:**

> Assign collector group to air policy

---

### `POST` clone

**Path:** `/management-rest/playbooks-policies/clone`

**Query params:** `newPolicyName`, `organization`, `sourcePolicyName`

**Description:**

> clone policy

---

### `GET` list-policies

**Path:** `/management-rest/playbooks-policies/list-policies`

**Query params:** `organization`

**Description:**

> List policies

---

### `PUT` map-connectors-to-actions

**Path:** `/management-rest/playbooks-policies/map-connectors-to-actions`

**Query params:** `organization`

**Body:** JSON body, fields: `policyName, customActionsToConnectorsMaps, fortinetActionsToConnectorsMaps`

**Description:**

> Assign policy actions with connectors.

---

### `PUT` set-action-classification

**Path:** `/management-rest/playbooks-policies/set-action-classification`

**Query params:** `organization`

**Body:** JSON body, fields: `policyName, customActionsToClassificationMaps, fortinetActionsToClassificationMaps`

**Description:**

> Set the air policy actions' classifications.

---

### `PUT` set-mode

**Path:** `/management-rest/playbooks-policies/set-mode`

**Query params:** `mode`, `organization`, `policyName`

**Description:**

> Set playbook to simulation/prevention

---

## management-rest / policies

| Method | Path | Name |
|---|---|---|
| `PUT` | `/management-rest/policies/assign-collector-group` | assign-collector-group |
| `POST` | `/management-rest/policies/clone` | clone |
| `GET` | `/management-rest/policies/list-policies` | list-policies |
| `POST` | `/management-rest/policies/scan-files` | scan-files |
| `PUT` | `/management-rest/policies/set-mode` | set-mode |
| `PUT` | `/management-rest/policies/set-policy-rule-action` | set-policy-rule-action |
| `PUT` | `/management-rest/policies/set-policy-rule-state` | set-policy-rule-state |

### `PUT` assign-collector-group

**Path:** `/management-rest/policies/assign-collector-group`

**Query params:** `collectorsGroupName`, `collectorsGroupName`, `forceAssign`, `organization`, `policyName`

**Description:**

> Assign collector group to policy

---

### `POST` clone

**Path:** `/management-rest/policies/clone`

**Query params:** `newPolicyName`, `organization`, `sourcePolicyName`

**Description:**

> clone policy

---

### `GET` list-policies

**Path:** `/management-rest/policies/list-policies`

**Query params:** `organization`

**Description:**

> List policies

---

### `POST` scan-files

**Path:** `/management-rest/policies/scan-files`

**Query params:** `applyRecursiveScan`, `executableFilesOnly`, `filePaths`, `filePaths`, `organization`, `origin`, `scanBy`, `scanSelection`, `scanSelection`

**Description:**

> Scan Files

---

### `PUT` set-mode

**Path:** `/management-rest/policies/set-mode`

**Query params:** `mode`, `organization`, `policyName`

**Description:**

> Set policy to simulation/prevention

---

### `PUT` set-policy-rule-action

**Path:** `/management-rest/policies/set-policy-rule-action`

**Query params:** `action`, `organization`, `policyName`, `ruleName`

**Description:**

> Set rule in policy to block/log

---

### `PUT` set-policy-rule-state

**Path:** `/management-rest/policies/set-policy-rule-state`

**Query params:** `organization`, `policyName`, `ruleName`, `state`

**Description:**

> Set rule in policy to enable/disable

---

## management-rest / sendable-entities

| Method | Path | Name |
|---|---|---|
| `PUT` | `/management-rest/sendable-entities/set-mail-format` | set-mail-format |
| `POST` | `/management-rest/sendable-entities/syslog` | syslog |

### `PUT` set-mail-format

**Path:** `/management-rest/sendable-entities/set-mail-format`

**Query params:** `format`, `organization`

**Description:**

> set mail format

---

### `POST` syslog

**Path:** `/management-rest/sendable-entities/syslog`

**Query params:** `organization`

**Body:** JSON body, fields: `host, name, organization, port, protocol, syslogFormat, syslogRFCFormat, certificateBlob, fazDevId, privateKeyFile, privateKeyPassword, useClientCertificate, useSSL`

**Description:**

> This API creates syslog

---

## management-rest / system-events

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/system-events/list-system-events` | list-system-events |

### `GET` list-system-events

**Path:** `/management-rest/system-events/list-system-events`

**Query params:** `componentNames`, `componentNames`, `componentTypes`, `fromDate`, `itemsPerPage`, `organization`, `pageNumber`, `sorting`, `strictMode`, `toDate`

**Description:**

> Retrieve system events

---

## management-rest / threat-hunting

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/threat-hunting/counts` | counts |
| `POST` | `/management-rest/threat-hunting/create-or-edit-tag` | create-or-edit-tag |
| `POST` | `/management-rest/threat-hunting/customize-fortinet-query` | customize-fortinet-query |
| `DELETE` | `/management-rest/threat-hunting/delete-saved-queries` | delete-saved-queries |
| `DELETE` | `/management-rest/threat-hunting/delete-syslog-server` | delete-syslog-server |
| `DELETE` | `/management-rest/threat-hunting/delete-tags` | delete-tags |
| `POST` | `/management-rest/threat-hunting/facets` | facets |
| `GET` | `/management-rest/threat-hunting/get-syslog-servers` | get-syslog-servers |
| `GET` | `/management-rest/threat-hunting/list-saved-queries` | list-saved-queries |
| `GET` | `/management-rest/threat-hunting/list-tags` | list-tags |
| `POST` | `/management-rest/threat-hunting/save-query` | save-query |
| `POST` | `/management-rest/threat-hunting/search` | search |
| `PUT` | `/management-rest/threat-hunting/set-query-state` | set-query-state |
| `POST` | `/management-rest/threat-hunting/test-syslog-server` | test-syslog-server |
| `POST` | `/management-rest/threat-hunting/update-syslog-server` | update-syslog-server |

### `POST` counts

**Path:** `/management-rest/threat-hunting/counts`

**Body:** JSON body, fields: `accountId, category, devices, filters, fromTime, itemsPerPage, organization, pageNumber, query, sorting, time, toTime`

**Description:**

> This API call outputs EDR total events for every EDR category

---

### `POST` create-or-edit-tag

**Path:** `/management-rest/threat-hunting/create-or-edit-tag`

**Body:** JSON body, fields: `newTagName, organization, tagId, tagName`

**Description:**

> This API creates or edits the saved queries tag

---

### `POST` customize-fortinet-query

**Path:** `/management-rest/threat-hunting/customize-fortinet-query`

**Query params:** `id`, `queryToEdit`

**Body:** JSON body, fields: `organization, dayOfMonth, dayOfWeek, forceSaving, frequency, frequencyUnit, fromTime, hour, scheduled, state, time, toTime`

**Description:**

> This API customizes the scheduling properties of a Fortinet query

---

### `DELETE` delete-saved-queries

**Path:** `/management-rest/threat-hunting/delete-saved-queries`

**Query params:** `deleteAll`, `deleteFromCommunity`, `organization`, `queryIds`, `queryIds`, `queryNames`, `queryNames`, `scheduled`, `source`

**Description:**

> This API deletes the saved queries

---

### `DELETE` delete-syslog-server

**Path:** `/management-rest/threat-hunting/delete-syslog-server`

**Query params:** `id`

**Description:**

> This API delete a syslog server

---

### `DELETE` delete-tags

**Path:** `/management-rest/threat-hunting/delete-tags`

**Query params:** `organization`, `tagIds`, `tagIds`, `tagNames`, `tagNames`

**Description:**

> This API deletes the saved queries tags

---

### `POST` facets

**Path:** `/management-rest/threat-hunting/facets`

**Body:** JSON body, fields: `facets, accountId, category, devices, filters, fromTime, itemsPerPage, organization, pageNumber, query, sorting, time, toTime`

**Description:**

> This API retrieves EDR total events for every EDR facet item

---

### `GET` get-syslog-servers

**Path:** `/management-rest/threat-hunting/get-syslog-servers`

**Query params:** `accountId`

**Description:**

> This API get the syslog servers

---

### `GET` list-saved-queries

**Path:** `/management-rest/threat-hunting/list-saved-queries`

**Query params:** `organization`, `scheduled`, `source`

**Description:**

> This API retrieves the existing saved queries list

---

### `GET` list-tags

**Path:** `/management-rest/threat-hunting/list-tags`

**Query params:** `organization`

**Description:**

> This API retrieves the existing saved queries tag list

---

### `POST` save-query

**Path:** `/management-rest/threat-hunting/save-query`

**Query params:** `id`, `queryToEdit`

**Body:** JSON body, fields: `organization, category, classification, collectorNames, community, dayOfMonth, dayOfWeek, description, forceSaving, frequency, frequencyUnit, fromTime, hour, name, query`...

**Description:**

> This API saves the query

---

### `POST` search

**Path:** `/management-rest/threat-hunting/search`

**Body:** JSON body, fields: `accountId, category, devices, filters, fromTime, itemsPerPage, organization, pageNumber, query, sorting, time, toTime`

**Description:**

> This API call outputs a list of Activity events from middleware.

---

### `PUT` set-query-state

**Path:** `/management-rest/threat-hunting/set-query-state`

**Query params:** `markAll`, `organization`, `queryIds`, `queryIds`, `queryNames`, `queryNames`, `source`, `state`

**Description:**

> This API updates the scheduled saved query state

---

### `POST` test-syslog-server

**Path:** `/management-rest/threat-hunting/test-syslog-server`

**Body:** JSON body, fields: `accountId, host, id, name, port, protocol, syslogRFCFormat, useSSL`

**Description:**

> This API test a syslog server connection

---

### `POST` update-syslog-server

**Path:** `/management-rest/threat-hunting/update-syslog-server`

**Body:** JSON body, fields: `accountId, agentGroupIds, host, id, name, port, protocol, syslogRFCFormat, useSSL`

**Description:**

> This API update a syslog server

---

## management-rest / threat-hunting-exclusions

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/threat-hunting-exclusions/exclusion` | exclusion |
| `PUT` | `/management-rest/threat-hunting-exclusions/exclusion` | exclusions |
| `DELETE` | `/management-rest/threat-hunting-exclusions/exclusion` | exclusion |
| `GET` | `/management-rest/threat-hunting-exclusions/exclusions-list` | exclusions-list |
| `POST` | `/management-rest/threat-hunting-exclusions/exclusions-list` | exclusions-list |
| `PUT` | `/management-rest/threat-hunting-exclusions/exclusions-list` | exclusions-list |
| `DELETE` | `/management-rest/threat-hunting-exclusions/exclusions-list` | exclusions-list |
| `GET` | `/management-rest/threat-hunting-exclusions/exclusions-metadata` | exclusions-metadata |
| `GET` | `/management-rest/threat-hunting-exclusions/exclusions-search` | exclusions-search |

### `POST` exclusion

**Path:** `/management-rest/threat-hunting-exclusions/exclusion`

**Body:** JSON body, fields: `exclusionListName, exclusions, organization`

**Description:**

> Creates exclusions.

---

### `PUT` exclusions

**Path:** `/management-rest/threat-hunting-exclusions/exclusion`

**Body:** JSON body, fields: `exclusionListName, exclusions, organization`

**Description:**

> Update exclusions.

---

### `DELETE` exclusion

**Path:** `/management-rest/threat-hunting-exclusions/exclusion`

**Body:** JSON body, fields: `exclusionIds, organization`

**Description:**

> Deletes one or more exclusions by Id.

---

### `GET` exclusions-list

**Path:** `/management-rest/threat-hunting-exclusions/exclusions-list`

**Query params:** `organization`

**Description:**

> Get the list of Exclusions lists.

---

### `POST` exclusions-list

**Path:** `/management-rest/threat-hunting-exclusions/exclusions-list`

**Body:** JSON body, fields: `name, organization, collectorGroupIds`

**Description:**

> Creates an exclusions list

---

### `PUT` exclusions-list

**Path:** `/management-rest/threat-hunting-exclusions/exclusions-list`

**Body:** JSON body, fields: `collectorGroupIds, listName, organization, newName`

**Description:**

> Updates an exclusions list

---

### `DELETE` exclusions-list

**Path:** `/management-rest/threat-hunting-exclusions/exclusions-list`

**Query params:** `listName`, `organization`

**Description:**

> Deletes an exclusions list.

---

### `GET` exclusions-metadata

**Path:** `/management-rest/threat-hunting-exclusions/exclusions-metadata`

**Description:**

> Get the metadata and available properties for exclusions configuration. When creating/modifying an exclusion, use the response of this API as a guide for the valid attribute names and values, and their corresponding EDR event types. Every attribute corresponds to an EDR category (for example, Filename attribute corresponds with the File category), and each category is a set of EDR event types.

---

### `GET` exclusions-search

**Path:** `/management-rest/threat-hunting-exclusions/exclusions-search`

**Query params:** `organization`, `os`, `os`, `searchText`

**Description:**

> Free-text search of exclusions

---

## management-rest / threat-hunting-settings

| Method | Path | Name |
|---|---|---|
| `GET` | `/management-rest/threat-hunting-settings/threat-hunting-metadata` | threat-hunting-metadata |
| `POST` | `/management-rest/threat-hunting-settings/threat-hunting-profile/collector-groups` | threat-hunting-profile-assign-collector-groups |
| `GET` | `/management-rest/threat-hunting-settings/threat-hunting-profile` | threat-hunting-profile |
| `POST` | `/management-rest/threat-hunting-settings/threat-hunting-profile` | threat-hunting-profile |
| `DELETE` | `/management-rest/threat-hunting-settings/threat-hunting-profile` | threat-hunting-profile |
| `POST` | `/management-rest/threat-hunting-settings/threat-hunting-profile-clone` | threat-hunting-profile-clone |

### `GET` threat-hunting-metadata

**Path:** `/management-rest/threat-hunting-settings/threat-hunting-metadata`

**Description:**

> Get the Threat Hunting Settings metadata object, listing the available configuration options (Category and Event Types).

---

### `POST` threat-hunting-profile-assign-collector-groups

**Path:** `/management-rest/threat-hunting-settings/threat-hunting-profile/collector-groups`

**Body:** JSON body, fields: `associatedCollectorGroupIds, name, organization`

**Description:**

> Update Threat Hunting profile assigned collector groups. Returns the updated list of assigned collector groups.

---

### `GET` threat-hunting-profile

**Path:** `/management-rest/threat-hunting-settings/threat-hunting-profile`

**Query params:** `organization`

**Description:**

> Get the list of Threat Hunting Setting profiles.

---

### `POST` threat-hunting-profile

**Path:** `/management-rest/threat-hunting-settings/threat-hunting-profile`

**Body:** JSON body, fields: `associatedCollectorGroupIds, name, organization, threatHuntingCategoryList, newName`

**Description:**

> Update Threat Hunting profile

---

### `DELETE` threat-hunting-profile

**Path:** `/management-rest/threat-hunting-settings/threat-hunting-profile`

**Query params:** `name`, `organization`

**Description:**

> Deletes a Threat Hunting profile.

---

### `POST` threat-hunting-profile-clone

**Path:** `/management-rest/threat-hunting-settings/threat-hunting-profile-clone`

**Query params:** `cloneProfileName`, `existingProfileName`, `organization`

**Description:**

> Clone a Threat Hunting Settings profile.

---

## management-rest / users

| Method | Path | Name |
|---|---|---|
| `POST` | `/management-rest/users/create-user` | create-user |
| `DELETE` | `/management-rest/users/delete-saml-settings` | delete-saml-settings |
| `DELETE` | `/management-rest/users/delete-user` | delete-user |
| `GET` | `/management-rest/users/get-sp-metadata` | get-sp-metadata |
| `GET` | `/management-rest/users/list-users` | list-users |
| `PUT` | `/management-rest/users/reset-password` | reset-password |
| `POST` | `/management-rest/users/update-saml-settings` | update-saml-settings |
| `PUT` | `/management-rest/users/update-user` | update-user |

### `POST` create-user

**Path:** `/management-rest/users/create-user`

**Query params:** `organization`

**Body:** JSON body, fields: `confirmPassword, email, firstName, lastName, password, role, username, customScript, remoteShell, restApi, title`

**Description:**

> This API create user in the system. (only for Admin role

---

### `DELETE` delete-saml-settings

**Path:** `/management-rest/users/delete-saml-settings`

**Query params:** `organizationNameRequest`

**Description:**

> Delete SAML authentication settings per organization

---

### `DELETE` delete-user

**Path:** `/management-rest/users/delete-user`

**Query params:** `organization`, `username`

**Description:**

> This API delete user from the system. Use the input parameters to filter organization

---

### `GET` get-sp-metadata

**Path:** `/management-rest/users/get-sp-metadata`

**Query params:** `organization`

**Description:**

> This API call retrieve the FortiEdr metadata by organization

---

### `GET` list-users

**Path:** `/management-rest/users/list-users`

**Query params:** `organization`

**Description:**

> This API call outputs a list of the users in the system. Use the input parameters to filter the list

---

### `PUT` reset-password

**Path:** `/management-rest/users/reset-password`

**Query params:** `organization`, `username`

**Body:** JSON body, fields: `confirmPassword, password`

**Description:**

> This API reset user password. Use the input parameters to filter organization

---

### `POST` update-saml-settings

**Path:** `/management-rest/users/update-saml-settings`

**Body:** form-data: idpMetadataFile

**Description:**

> Create / Update SAML authentication settings per organization

---

### `PUT` update-user

**Path:** `/management-rest/users/update-user`

**Query params:** `organization`, `username`

**Body:** JSON body, fields: `email, firstName, lastName, role, username, customScript, remoteShell, restApi, title`

**Description:**

> This API update user in the system. Use the input parameters to filter organization

---
