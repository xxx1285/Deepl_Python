package main

import (
	"bufio"
	"os"
	"regexp"
	"strings"
)

func extractUrlsFromFile(inputPath string) []string {
	file, err := os.Open(inputPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	text := ""
	for scanner.Scan() {
		text += scanner.Text() + " "
	}

	potentialUrls := strings.Fields(text)
	urlPattern := regexp.MustCompile(`https?://\S+`)
	validUrls := []string{}

	for _, url := range potentialUrls {
		if urlPattern.MatchString(url) {
			validUrls = append(validUrls, url)
		}
	}

	return validUrls
}

func saveToFile(urls []string, outputPath string) {
	file, err := os.Create(outputPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	for _, url := range urls {
		writer.WriteString(url + "\n")
	}
	writer.Flush()
}

func main() {
	inputPath := "Linkbilding/Google_tables_URL_chistim/input/source.txt"
	outputPath := "Linkbilding/Google_tables_URL_chistim/output/urls.txt"

	urls := extractUrlsFromFile(inputPath)
	saveToFile(urls, outputPath)
}
