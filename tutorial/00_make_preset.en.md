# Define Motors in `preset.json`

- Next Tutorial: [Torque On/Off](01_torque.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)

---


```json
{
  "ports":[  ],
  "baud rates":[  ],
  "protocol versions":[  ],
  "motors":[  ]
}
```

1. "ports"
1. "baud rates"
1. "protocol versions"
1. "motors"

```json
{
  "ports":[ "/dev/ttyUSB0" ],
  "baud rates":[ 57600 ],
  "protocol versions":[ 2.0 ],
  "motors":[
    {
      "id": 0,
      "alias": "joint_1",
      "model": "XM430-W210"
    }
  ]
}
```

---

- Next Tutorial: [Torque On/Off](01_torque.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)
