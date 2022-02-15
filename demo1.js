      treeData=JSON.parse(jsonstr);
       treeJson = d3.json("data.json", function(error, treeData) {
        treeData=JSON.parse(jsonstr);
      	dTree.init(treeData,
                                        {
                                                target: "#graph",
                                                debug: true,
                                                hideMarriageNodes: true,
                                                marriageNodeSize: 5,
                                                height: 800,
                                                width: 1200,
                                                callbacks: {
                                                        nodeClick: function(name, extra) {
                                                        },
                                                        nodeRightClick: function(name, extra) {
                                                        },
                                                        textRenderer: function(name, extra, textClass) {
                                                                if (extra && extra.nickname)
                                                                        name = name + " (" + extra.nickname + ")";
                                                                return "<p align='center' class='" + textClass + "'>" + name + "</p>";
                                                        },
                                                        marriageClick: function(extra, id) {
                                                                alert('Clicked marriage node' + id);
                                                        },
                                                        marriageRightClick: function(extra, id) {
                                                                alert('Right-clicked marriage node' + id);
                                                        },
                                                }
                                        });
});
