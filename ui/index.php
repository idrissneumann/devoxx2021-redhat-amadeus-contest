<!DOCTYPE html>
<?php
	$api_url = getenv('API_URL');
	$api_url_inside_container = getenv('API_URL_INSIDE_CONTAINER');
?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
    <head>
        <title>AmadeusSearch</title>
        <link type="text/css" href="/js/jquery/1.8/css/jquery-ui-1.8.custom.css" rel="Stylesheet" />
        <link type="text/css" href="/style/css/datatable.css" rel="Stylesheet" />
        <link type="text/css" href="/style/css/main.css" rel="Stylesheet" />
        <script type="text/javascript" src="/js/jquery/1.7/jquery.min.js"></script>
        <script type="text/javascript" src="/js/jquery/1.8/jquery-ui.min.js"></script>
        <script type="text/javascript" src="/js/jquery/1.8/jquery.dataTables.js"></script>
        <script type="text/javascript" src="/js/main.js"></script>
    </head>
    <body>
        <div class="appContent">
            <h1>Amadeus search</h1>
            <?php
                $airports = json_decode(file_get_contents($api_url_inside_container . "/v1/airports"), true);
            ?>

            <form name="frmSearch" id="frmSearch" onsubmit="loadFlights('<?php echo $api_url; ?>'); return false;">
                Origin: <select id="origin">
                <?php
                    foreach ($airports as $code => $name) {
                        echo "<option value=\"$code\">$name</option>";
                    }
                ?>
                </select>&nbsp;
				
                Destination: <select id="destination">
                <?php
                    foreach ($airports as $code => $name) {
                        echo "<option value=\"$code\">$name</option>";
                    }
                ?>
                </select>&nbsp;
				
                Departure date: <select id="departure_date">
                <?php
                    $current_date = date("Y-m-d");
                    for ($i = 0 ; $i < 10 ; $i++) {
                        $onedaymore = date("Y-m-d", strtotime("1 day", strtotime($current_date)));
                        echo "<option value=\"$onedaymore\">$onedaymore</option>";
                        $current_date = $onedaymore;
                    }
                ?>
                </select>&nbsp;
                <input name="count" type="button" value="Search" onclick="loadFlights('<?php echo $api_url; ?>');">
            </form>
			<br />
		    <div id="contentTable"></div>
		</div>
	</body>
</html>
