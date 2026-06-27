# Sample Catalog

Source directory:

`C:\Users\26561\Desktop\模型训练资料\甲方提供资料`

The files below are indexed for future validation. They are not copied into Git because several are large binary documents or generated image batches.

## Candidate Tender Files

| File | Size | Suggested Use |
| --- | ---: | --- |
| `202507251108191419招标文件.doc` | 491 KB | Legacy Word tender sample; useful for later doc conversion compatibility. |
| `KSDQZFCG（GK）2026-64喀什大学重大设备更新（5.4人工智能数据抓取及衍生智能服务创新平台-多场景应用系统-人力资源管理平台(一期））项目（二次）.docx` | 606 KB | Modern docx tender sample; good candidate for Phase 2 parsing. |

## Candidate Historical Bid Files

| File | Size | Suggested Use |
| --- | ---: | --- |
| `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx` | 1.1 MB | Small historical bid docx; preferred early parsing sample. |
| `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.pdf` | 2.3 MB | Matching PDF; useful for pdf parsing comparison. |
| `宁波运维项目\牧鸿\省人事工资管理服务系统-宁波人社运维-资格证明文件.docx` | 163 KB | Small qualification-material sample; useful for out-of-scope boundary checks. |
| `宁波运维项目\九州拓新\九州拓新-资格文件.docx` | 3.0 MB | Qualification material; use only after bid-text parsing works. |
| `宁波运维项目\九州拓新\九州拓新-投标书.docx` | 37 MB | Large historical bid file; defer until parser memory behavior is known. |
| `宁波运维项目\浙江速微科技有限公司\浙江速微科技有限公司-投标书.docx` | 18 MB | Large historical bid file; defer until parser memory behavior is known. |
| `5.25-带报价-喀什文件-九州拓新(1).docx` | 194 MB | Very large sample; do not use in early smoke tests. |

## Image And Scanned Material

| Path | Suggested Use |
| --- | --- |
| `宁波运维项目\九州拓新\批量输出为图片\...` | Future OCR and scanned-page validation. |
| `宁波运维项目\浙江速微科技有限公司\批量输出为图片\...` | Future OCR and scanned-page validation. |
| `宁波运维项目\浙江速微科技有限公司\社保证明8.11(1)\...` | Qualification evidence; useful for out-of-scope and risk handling tests. |

## Other Material

| File | Size | Suggested Use |
| --- | ---: | --- |
| `2026年-投标智能-开发计划-技术补充版.xlsx` | 38 KB | Later planning/reference material; inspect before turning into requirements. |
| `detailQA.docx` | 14 KB | Later Q&A/reference material; inspect before using as acceptance criteria. |
| `宁波运维项目.rar` | 229 MB | Archive copy; do not ingest directly while source folder exists. |

## Recommended First Validation Set

Use this set after Phase 1 is complete and Phase 2 begins:

1. Tender: `KSDQZFCG（GK）2026-64...docx`
2. Historical bid: `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.docx`
3. Historical bid PDF comparison: `宁波运维项目\牧鸿\省人事工资管理服务系统宁波人社运维投标文件-投标书.pdf`

Avoid the 18 MB, 37 MB, 194 MB, and 229 MB files until parser behavior and timeout limits are known.
