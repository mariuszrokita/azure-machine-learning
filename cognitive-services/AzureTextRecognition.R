library(httr)
library(rjson)

source("AzureConfig.R")

#' Get results of text recognition by calling Azure Bing Visual Search OCR API.
#'
#' @param filePath A path to an image file.
#' @return A list of strings (text recognized on provided image).
getBingOCR <- function(filePath) {

  # Rest call to API
  resp <- POST(url = BING_BASE_URI,
               add_headers('Ocp-Apim-Subscription-Key' = BING_ACCESS_KEY,
                           'Accept' = 'application/json'),
               body = list(image = upload_file(file_path)))

  # parse Json and collect text recognitions
  json_data <- fromJSON(content(resp, as="text"))
  recognized_texts <- list()
  for (tag in json_data$tags) {
    for (action in tag$actions) {
      if (!is.null(action$`_type`) && action$`_type` == "ImageKnowledge/TextRecognitionAction") {
        for (region in action$data$regions) {
          for (line in region$lines) {
            for (word in line$words) {
              recognized_texts = append(recognized_texts, word$text)
            }
          }
        }
      }
    }
  }

  return(recognized_texts)
}

#' Get results of text recognition by calling Azure Computer Vision OCR API.
#'
#' @param filePath A path to an image file.
#' @return A list of strings (text recognized on provided image).
getComputerVisionOCR <- function(file_path) {
  # Rest call to API
  resp <- POST(url = COMPUTERVISION_BASE_URI,
               add_headers('Ocp-Apim-Subscription-Key' = COMPUTERVISION_ACCOUNT_KEY,
                           'Accept' = 'application/json'),
               body = list(image = upload_file(file_path))) 

  # parse Json and collect text recognitions
  resp_text <- content(resp, as="text")
  json_data <- fromJSON(resp_text)
  recognized_texts <- list()
  for (region in json_data$regions) {
    for (line in region$lines) {
      for (word in line$words) {
        recognized_texts = append(recognized_texts, word$text)
      }
    }
  }

  return(recognized_texts)
}
