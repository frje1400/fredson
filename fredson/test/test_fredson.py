import json

from fredson import fredson_parse


def test_parse_simple():
    simple = '{"foo":"bar"}'
    assert fredson_parse(simple) == {'foo': 'bar'}


def test_parse_nested():
    nested = '{"foo":{"bar":"baz"}}'
    assert fredson_parse(nested) == {'foo': {'bar': 'baz'}}


def test_parse_empty_obj():
    assert fredson_parse("""{"foo":{}}""") == {'foo': {}}


def test_parse_simple_list():
    simple_list = '{"foo": ["bar"]}'
    assert fredson_parse(simple_list) == {'foo': ['bar']}


def test_parse_empty_list():
    assert fredson_parse("""{"foo":[]}""") == {'foo': []}


def test_parse_two_item_list():
    two_items = '{"foo": ["bar", "baz"]}'
    assert fredson_parse(two_items) == {'foo': ['bar', 'baz']}


def test_parse_multi_line():
    multi_line = """
    {
    "foo":
        [
        "bar",
        "baz"
        ]
    }
    """
    assert fredson_parse(multi_line) == {'foo': ['bar', 'baz']}


def test_parse_nested_lists():
    nested_lists = """
    {
      "foo": [
        {
          "bar": [
            "baz",
            "qxc",
            "abc"
          ]
        }
      ]
    }
    """
    assert fredson_parse(nested_lists) == {'foo': [{'bar': ['baz', 'qxc', 'abc']}]}


def test_parse_multiple_keys():
    multiple_keys = """
    {
        "foo": "bar",
        "baz": "boo"
    }
    """
    assert fredson_parse(multiple_keys) == {'foo': 'bar', 'baz': 'boo'}, f"actual: {fredson_parse(multiple_keys)}"


def test_multiple_keys_nested_list():
    multiple_keys_nested_list = """
    {
      "foo": [
        {
          "bar": [
            "baz",
            "qxc",
            "abc"
          ]
        }
      ],
      "uvw": "qxas",
      "vghj": "nja",
      "oasfa": {
        "asc": "asarera",
        "dgdjkj": "deijij",
        "iuiuij": "hihih"
      }
    }
    """
    assert fredson_parse(multiple_keys_nested_list) == json.loads(multiple_keys_nested_list)


def test_parse_simple_numbers():
    simple_numbers = """
    { "number": 123 }
    """
    assert fredson_parse(simple_numbers) == json.loads(simple_numbers)


def test_parse_simple_numbers_fraction():
    simple_numbers_fraction = """
    { "number": 123.456 }
    """
    assert fredson_parse(simple_numbers_fraction) == json.loads(simple_numbers_fraction)


def test_parse_fraction_exponent():
    simple_numbers_fraction_exponent = """ { "number": 123.456e+12 } """
    assert fredson_parse(simple_numbers_fraction_exponent) == json.loads(simple_numbers_fraction_exponent)


def test_parse_bool_false():
    false = """ { "bool": false } """
    assert fredson_parse(false) == json.loads(false)


def test_parse_bool_true():
    true = """ { "bool": true } """
    assert fredson_parse(true) == json.loads(true)


def test_parse_bool_null():
    null = """ { "bool": null } """
    assert fredson_parse(null) == json.loads(null)


def test_parse_single_quotation():
    assert fredson_parse("""{"foo": "\\""}""") == {'foo': '"'}


def test_parse_unicode_escape():
    assert fredson_parse('{"foo": "\\u0063"}') == {'foo': 'c'}


def test_parse_newline():
    newline = '{"foo": "\\n"}'
    assert fredson_parse(newline) == {'foo': '\n'}


def test_json_example_1():
    # https://json.org/example.html
    example = """
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                 "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                         "SortAs": "SGML",
                         "GlossTerm": "Standard Generalized Markup Language",
                         "Acronym": "SGML",
                         "Abbrev": "ISO 8879:1986",
                         "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                              "GlossSeeAlso": ["GML", "XML"]
                        },
                         "GlossSee": "markup"
                    }
                }
            }
        }
    } 
    """
    assert fredson_parse(example) == json.loads(example)


def test_json_example_2():
    # https://json.org/example.html
    example = """
    {"menu": {
      "id": "file",
      "value": "File",
      "popup": {
        "menuitem": [
          {"value": "New", "onclick": "CreateNewDoc()"},
          {"value": "Open", "onclick": "OpenDoc()"},
          {"value": "Close", "onclick": "CloseDoc()"}
        ]
      }
    }}
    """
    assert fredson_parse(example) == json.loads(example)


def test_json_example_3():
    # https://json.org/example.html
    example = """
    {"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
    }}    
    """
    assert fredson_parse(example) == json.loads(example)


def test_json_example_4():
    # https://json.org/example.html
    example = """
    {"web-app": {
  "servlet": [   
    {
      "servlet-name": "cofaxCDS",
      "servlet-class": "org.cofax.cds.CDSServlet",
      "init-param": {
        "configGlossary:installationAt": "Philadelphia, PA",
        "configGlossary:adminEmail": "ksm@pobox.com",
        "configGlossary:poweredBy": "Cofax",
        "configGlossary:poweredByIcon": "/images/cofax.gif",
        "configGlossary:staticPath": "/content/static",
        "templateProcessorClass": "org.cofax.WysiwygTemplate",
        "templateLoaderClass": "org.cofax.FilesTemplateLoader",
        "templatePath": "templates",
        "templateOverridePath": "",
        "defaultListTemplate": "listTemplate.htm",
        "defaultFileTemplate": "articleTemplate.htm",
        "useJSP": false,
        "jspListTemplate": "listTemplate.jsp",
        "jspFileTemplate": "articleTemplate.jsp",
        "cachePackageTagsTrack": 200,
        "cachePackageTagsStore": 200,
        "cachePackageTagsRefresh": 60,
        "cacheTemplatesTrack": 100,
        "cacheTemplatesStore": 50,
        "cacheTemplatesRefresh": 15,
        "cachePagesTrack": 200,
        "cachePagesStore": 100,
        "cachePagesRefresh": 10,
        "cachePagesDirtyRead": 10,
        "searchEngineListTemplate": "forSearchEnginesList.htm",
        "searchEngineFileTemplate": "forSearchEngines.htm",
        "searchEngineRobotsDb": "WEB-INF/robots.db",
        "useDataStore": true,
        "dataStoreClass": "org.cofax.SqlDataStore",
        "redirectionClass": "org.cofax.SqlRedirection",
        "dataStoreName": "cofax",
        "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
        "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
        "dataStoreUser": "sa",
        "dataStorePassword": "dataStoreTestQuery",
        "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
        "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
        "dataStoreInitConns": 10,
        "dataStoreMaxConns": 100,
        "dataStoreConnUsageLimit": 100,
        "dataStoreLogLevel": "debug",
        "maxUrlLength": 500}},
    {
      "servlet-name": "cofaxEmail",
      "servlet-class": "org.cofax.cds.EmailServlet",
      "init-param": {
      "mailHost": "mail1",
      "mailHostOverride": "mail2"}},
    {
      "servlet-name": "cofaxAdmin",
      "servlet-class": "org.cofax.cds.AdminServlet"},
 
    {
      "servlet-name": "fileServlet",
      "servlet-class": "org.cofax.cds.FileServlet"},
    {
      "servlet-name": "cofaxTools",
      "servlet-class": "org.cofax.cms.CofaxToolsServlet",
      "init-param": {
        "templatePath": "toolstemplates/",
        "log": 1,
        "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
        "logMaxSize": "",
        "dataLog": 1,
        "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
        "dataLogMaxSize": "",
        "removePageCache": "/content/admin/remove?cache=pages&id=",
        "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
        "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
        "lookInContext": 1,
        "adminGroupID": 4,
        "betaServer": true}}],
  "servlet-mapping": {
    "cofaxCDS": "/",
    "cofaxEmail": "/cofaxutil/aemail/*",
    "cofaxAdmin": "/admin/*",
    "fileServlet": "/static/*",
    "cofaxTools": "/tools/*"},
 
  "taglib": {
    "taglib-uri": "cofax.tld",
    "taglib-location": "/WEB-INF/tlds/cofax.tld"}}}
    """
    assert fredson_parse(example) == json.loads(example)


def test_json_example_5():
    # https://json.org/example.html
    example = """
    {"menu": {
    "header": "SVG Viewer",
    "items": [
        {"id": "Open"},
        {"id": "OpenNew", "label": "Open New"},
        null,
        {"id": "ZoomIn", "label": "Zoom In"},
        {"id": "ZoomOut", "label": "Zoom Out"},
        {"id": "OriginalView", "label": "Original View"},
        null,
        {"id": "Quality"},
        {"id": "Pause"},
        {"id": "Mute"},
        null,
        {"id": "Find", "label": "Find..."},
        {"id": "FindAgain", "label": "Find Again"},
        {"id": "Copy"},
        {"id": "CopyAgain", "label": "Copy Again"},
        {"id": "CopySVG", "label": "Copy SVG"},
        {"id": "ViewSVG", "label": "View SVG"},
        {"id": "ViewSource", "label": "View Source"},
        {"id": "SaveAs", "label": "Save As"},
        null,
        {"id": "Help"},
        {"id": "About", "label": "About Adobe CVG Viewer..."}
    ]
    }}
    """
    assert fredson_parse(example) == json.loads(example)
