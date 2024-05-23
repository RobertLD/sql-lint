SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO

CREATE VIEW dbo.[vw_HighTouchTrade] AS (
    SELECT
        discretionarytradeid AS hightouchtradeid,
        discretionarytradedescription AS hightouchtradedescription,
        discretionarytradetypeid AS hightouchtradetypeid,
        ordersdetailid,






        holduntiltradedate,
        createdby,
        createddate,
        orderguid
    FROM
        dbo.discretionarytrade
)
GO
