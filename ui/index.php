<!DOCTYPE html>
<?php
	$api_url = getenv('API_URL');
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
			<form name="frmSearch" id="frmSearch" onsubmit="loadFlights('<?php echo $api_url; ?>'); return false;">
				Origin : <select id="origin">
					<option value="SYD">Sydney</option>
					<option value="BKK">Bankok</option>
					<option value="SIN">Singapor</option>
					<option value="HKG">Hong Kong</option>
					<option value="CDG">Paris CDG</option>
				</select>&nbsp;
				Destination : <select id="destination">
					<option value="SYD">Sydney</option>
					<option value="BKK">Bankok</option>
					<option value="SIN">Singapor</option>
					<option value="HKG">Hong Kong</option>
					<option value="CDG">Paris CDG</option>
				</select>&nbsp;
				Departure date : <select id="departure_date">
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
			<div id="contentTable">
			</div>
		</div>
	</body>
</html>