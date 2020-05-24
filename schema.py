schema= {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#", 
	"$id": "https://example.com/object1590289101.json", 
	"title": "Root", 
	"type": "object",
	"required": [
		"source",
		"type",
		"cves"
	],
	"properties": {
		"source": {
			"$id": "#root/source", 
			"title": "Source", 
			"type": "string",
			"default": "",
			"examples": [
				"adobe"
			],
			"pattern": "^.*$"
		},
		"type": {
			"$id": "#root/type", 
			"title": "Type", 
			"type": "string",
			"default": "",
			"examples": [
				"vendor"
			],
			"pattern": "^.*$"
		},
		"cves": {
			"$id": "#root/cves", 
			"title": "Cves", 
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/cves/items", 
				"title": "Items", 
				"type": "object",
				"required": [
					"timestamp",
					"id",
					"url",
					"name",
					"description"
				],
				"properties": {
					"timestamp": {
						"$id": "#root/cves/items/timestamp", 
						"title": "Timestamp", 
						"type": "string",
						"default": "",
						"examples": [
							"2020-03-12T18:06Z"
						],
						"pattern": "^.*$"
					},
					"published_date": {
						"$id": "#root/cves/items/published_date", 
						"title": "Published_date", 
						"type": "string",
						"default": "",
						"examples": [
							"2020-01-14T00:00Z"
						],
						"pattern": "^.*$"
                    },
                    "last_modified_date": {
						"$id": "#root/cves/items/last_modified_date", 
						"title": "last_modified_date", 
						"type": "string",
						"default": "",
						"examples": [
							"2020-01-14T00:00Z"
						],
						"pattern": "^.*$"
					},
					"id": {
						"$id": "#root/cves/items/id", 
						"title": "Id", 
						"type": "string",
						"default": "",
						"examples": [
							"CVE-2019-16466"
						],
						"pattern": "^.*$"
					},
					"url": {
						"$id": "#root/cves/items/url", 
						"title": "Url", 
						"type": "string",
						"default": "",
						"examples": [
							"https://helpx.adobe.com/security/products/experience-manager/apsb20 - 01. html "
						],
						"pattern": "^.*$"
					},
					"name": {
						"$id": "#root/cves/items/name", 
						"title": "Name", 
						"type": "string",
						"default": "",
						"examples": [
							"APSB20-01 Security update available for Adobe Experience Manager"
						],
						"pattern": "^.*$"
					},
					"description": {
						"$id": "#root/cves/items/description", 
						"title": "Description", 
						"type": "string",
						"default": "",
						"examples": [
							"cross-site script inclusion"
						],
						"pattern": "^.*$"
					},
					"cpes": {
						"$id": "#root/cves/items/cpes", 
						"title": "Cpes", 
						"type": "object",
						"required": [
							"operator",
							"cpe_list"
						],
						"properties": {
							"operator": {
								"$id": "#root/cves/items/cpes/operator", 
								"title": "Operator", 
								"type": "string",
								"default": "",
								"examples": [
									"OR"
								],
								"pattern": "^.*$"
							},
							"cpe_list": {
								"$id": "#root/cves/items/cpes/cpe_list", 
								"title": "Cpe_list", 
								"type": "array",
								"default": [],
								"items":{
									"$id": "#root/cves/items/cpes/cpe_list/items", 
									"title": "Items", 
									"type": "object",
									"required": [
										"vendor",
										"product",
										"category"
									],
									"properties": {
										"vendor": {
											"$id": "#root/cves/items/cpes/cpe_list/items/vendor", 
											"title": "Vendor", 
											"type": "string",
											"default": "",
											"examples": [
												"adobe"
											],
											"pattern": "^.*$"
										},
										"product": {
											"$id": "#root/cves/items/cpes/cpe_list/items/product", 
											"title": "Product", 
											"type": "string",
											"default": "",
											"examples": [
												"experience_manager"
											],
											"pattern": "^.*$"
										},
										"category": {
											"$id": "#root/cves/items/cpes/cpe_list/items/category", 
											"title": "Category", 
											"type": "string",
											"default": "",
											"examples": [
												"a"
											],
											"pattern": "^.*$"
										},
										"versionStartIncluding": {
											"$id": "#root/cves/items/cpes/cpe_list/items/versionStartIncluding", 
											"title": "Versionstartincluding", 
											"type": "string",
											"default": "",
											"examples": [
												"6.0"
											],
											"pattern": "^.*$"
										},
										"versionEndIncluding": {
											"$id": "#root/cves/items/cpes/cpe_list/items/versionEndIncluding", 
											"title": "Versionendincluding", 
											"type": "string",
											"default": "",
											"examples": [
												"6.5"
											],
											"pattern": "^.*$"
                                        },
                                        "versionStartExcluding": {
											"$id": "#root/cves/items/cpes/cpe_list/items/versionStartExcluding", 
											"title": "versionStartExcluding", 
											"type": "string",
											"default": "",
											"examples": [
												"6.0"
											],
											"pattern": "^.*$"
										},
										"versionEndExcluding": {
											"$id": "#root/cves/items/cpes/cpe_list/items/versionEndExcluding", 
											"title": "versionEndExcluding", 
											"type": "string",
											"default": "",
											"examples": [
												"6.5"
											],
											"pattern": "^.*$"
                                        },
                                        "update": {
											"$id": "#root/cves/items/cpes/cpe_list/items/update", 
											"title": "update", 
											"type": "string",
											"default": "",
											"examples": [
												"6.0"
											],
											"pattern": "^.*$"
										},
										"sw_version": {
											"$id": "#root/cves/items/cpes/cpe_list/items/sw_version", 
											"title": "sw_version", 
											"type": "string",
											"default": "",
											"examples": [
												"6.5"
											],
											"pattern": "^.*$"
                                        },
                                        "patches":{
                                            "$id": "#root/cves/items/cpes/patches", 
                                            "title": "patches", 
                                            "type": "array",
                                            "default": [],
                                            "examples": [
                                                "123", "234"
                                            ]
                                        },
										"cpe23Uri": {
											"$id": "#root/cves/items/cpes/cpe_list/items/cpe23Uri", 
											"title": "Cpe23uri", 
											"type": "string",
											"default": "",
											"examples": [
												"cpe:2.3:a:adobe:experience_manager:*:*:*:*:*:*:*:*"
											],
											"pattern": "^.*$"
										}
									}
								}

							}
						}
					}
,
					"cvssv2": {
						"$id": "#root/cves/items/cvssv2", 
						"title": "Cvssv2", 
						"type": "object",
						"required": [],
						"properties": {
							"severity": {
								"$id": "#root/cves/items/cvssv2/severity", 
								"title": "Severity", 
								"type": "string",
								"default": "",
								"examples": [
									"HIGH"
								],
								"pattern": "^.*$"
                            },
                            "'vector_string": {
								"$id": "#root/cves/items/cvssv2/vector_string", 
								"title": "vector_string", 
								"type": "string",
								"default": "",
								"examples": [
									"HIGH"
								],
								"pattern": "^.*$"
                            },
                            "base_score": {
								"$id": "#root/cves/items/cvssv2/base_score", 
								"title": "base_score", 
								"type": "string",
								"default": "",
								"examples": [
									"HIGH"
								],
								"pattern": "^.*$"
							}
						}
					}
,
					"cvssv3": {
						"$id": "#root/cves/items/cvssv3", 
						"title": "Cvssv3", 
						"type": "object",
						"required": [],
						"properties": {
							"severity": {
								"$id": "#root/cves/items/cvssv2/severity", 
								"title": "Severity", 
								"type": "string",
								"default": "",
								"examples": [
									"HIGH"
								],
								"pattern": "^.*$"
                            },
                            "'vector_string": {
								"$id": "#root/cves/items/cvssv2/vector_string", 
								"title": "vector_string", 
								"type": "string",
								"default": "",
								"examples": [
									"HIGH"
								],
								"pattern": "^.*$"
                            },
                            "base_score": {
								"$id": "#root/cves/items/cvssv2/base_score", 
								"title": "base_score", 
								"type": "string",
								"default": "",
								"examples": [
									"HIGH"
								],
								"pattern": "^.*$"
							}
						}
                    },
                    "patches": {
						"$id": "#root/cves/items/patches", 
						"title": "patches", 
						"type": "object",
                        "required": [],
                        "properties": {
                            "patch_id": {
                                "$id": "#root/patches/items/patch_id", 
                                "title": "Patch_id", 
                                "type": "integer",
                                "examples": [
                                    123
                                ],
                                "default": 0
                            },
                            "reference": {
                                "$id": "#root/patches/items/reference", 
                                "title": "Reference", 
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "www.google.com"
                                ],
                                "pattern": "^.*$"
                            },
                            "supersedes": {
                                "$id": "#root/patches/items/supersedes", 
                                "title": "Supersedes", 
                                "type": "array",
                                "default": [],
                                "items":{
                                    "$id": "#root/patches/items/supersedes/items", 
                                    "title": "Items", 
                                    "type": "integer",
                                    "examples": [
                                        1
                                    ],
                                    "default": 0
                                }
                            },
                            "restart_needed": {
                                "$id": "#root/patches/items/restart_needed", 
                                "title": "Restart_needed", 
                                "type": "boolean",
                                "examples": [
                                    'true'
                                ],
                                "default": 'true'
                            },
                            "patch_type": {
                                "$id": "#root/patches/items/patch_type", 
                                "title": "Patch_type", 
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "xyz"
                                ],
                                "pattern": "^.*$"
                            },
                            "release_date": {
                                "$id": "#root/patches/items/release_date", 
                                "title": "Release_date", 
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "2020-03-12T18:06Z"
                                ],
                                "pattern": "^.*$"
                            }
                        }
                    }

				}
			}

		}
	}
}
