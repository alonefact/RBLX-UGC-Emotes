## Overview

This repository contains a compiled list of **Roblox UGC emotes** gathered from the Roblox catalog. The goal is to provide researchers and developers with a structured dataset for analysis.

> [!NOTE]
> Some emotes don't appear in the Roblox API and are therefore not included in this list.

---

## Stats

| Metric | Value |
|--------|-------|
| Total Emotes | 59,507 |
| Unique Creators | 14,096 |
| Estimated Cost (Publishing + Uploading) | 126,882,000 Robux (~$482,146.60 USD) |
| Data Collected | May 1, 2026 |

---

## Data Structure

```json
{
  "CreatorName": "string",
  "CreatorId": "number",
  "EmoteName": "string",
  "Description": "string",
  "ItemId": "number"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `CreatorName` | `string` | Display name of the UGC creator |
| `CreatorId` | `number` | Roblox user ID of the creator |
| `EmoteName` | `string` | Name of the emote as listed on the catalog |
| `Description` | `string` | Item description provided by the creator |
| `ItemId` | `number` | Unique Roblox catalog item ID |

---

## Disclaimer

This project is intended purely for **research and educational purposes**. It aims to provide a general understanding of the current state of Roblox UGC emotes. This repository is not affiliated with or endorsed by Roblox Corporation.
