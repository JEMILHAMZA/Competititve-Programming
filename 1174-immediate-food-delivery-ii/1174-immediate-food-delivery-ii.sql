# Write your MySQL query statement below
WITH FirstOrders AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM
        Delivery
    GROUP BY
        customer_id
),
ImmediateOrders AS (
    SELECT
        F.customer_id,
        D.delivery_id,
        D.order_date,
        D.customer_pref_delivery_date
    FROM
        FirstOrders F
    JOIN
        Delivery D
    ON
        F.customer_id = D.customer_id
        AND F.first_order_date = D.order_date
)
SELECT
    ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS immediate_percentage
FROM
    ImmediateOrders;
