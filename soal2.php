<?php
namespace Facebook\WebDriver;

require_once('vendor/autoload.php');

use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\Remote\DesiredCapabilities;

$serverUrl = 'http://localhost:4444';
$driver = RemoteWebDriver::create($serverUrl, DesiredCapabilities::firefox(), 60*1000, 60*1000);

$driver->get('https://bukalapak.com/');

$driver->wait(10, 500)->until(
	WebDriverExpectedCondition::titleContains('Bukalapak')
);

$search_term = 'Filter Oli';

$driver->findElement(WebDriverBy::id("v-omnisearch__input"))->sendKeys($search_term);
$driver->findElement(WebDriverBy::cssSelector('.v-omnisearch__submit'))->click();

$driver->wait(10, 500)->until(
	WebDriverExpectedCondition::titleContains($search_term)
);

$search_title = $driver->findElement(WebDriverBy::cssSelector('h1.bl-text--subheading-3'))->getText();
assert(strpos($search_title, $search_term) > 0, 'Search result page not opened');

$total_product = $driver->findElement(WebDriverBy::cssSelector('.te-total-products'))->getText();
$total_product = explode(' ', $total_product);
$total_product = intval(str_replace('.', '', $total_product[0]));

assert($total_product > 0, 'Total product is not greater than 0');

$driver->quit();
