module Main exposing (..)

import Html exposing (..)


-- MODEL


type alias Model =
    {}



-- UPDATE


type Msg
    = Reset


update : Msg -> Model -> Model
update msg model =
    case msg of
        Reset ->
            model



-- VIEW
-- view : Model -> Html Msg
-- view model =
